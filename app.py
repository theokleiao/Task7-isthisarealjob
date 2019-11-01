# ''' Deploy user recomender model using flask framework'''

# Import Relevant Modules
try:
    import pickle
    import joblib
    from flask import Flask, request, render_template
    import pandas as pd
    from difflib import get_close_matches
    import requests
    from bs4 import BeautifulSoup
except ImportError as i_error:
    print(i_error)

# Load the datasets needed for deployment
cac_db = pd.read_csv('data/cac_db.csv')
# cac_db['name'] = cac_db.name.str.lower()

# load the model from disk
classifier = joblib.load('data/classifier.sav')


def search(word):
    word = word.upper()

    def start(x):
        if x.startswith(word):
            return True
        else:
            return False

    if len(cac_db[cac_db['COMPANY NAME'].apply(start)]) > 0:
        return cac_db[cac_db['COMPANY NAME'].apply(start)].head(5)
    elif len(get_close_matches(word, cac_db['COMPANY NAME'], 5, cutoff=0.7)) > 0:
        return get_close_matches(word, cac_db['COMPANY NAME'], 5, cutoff=0.7)
    else:
        return ["Not in CAC database"]


def scrape(company_name):
    cn = company_name.split()
    cn = '+'.join(cn)
    url = f"https://www.nairaland.com/search?q={cn}&board=0"
    scrape = requests.get(url, headers={'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"})
    page = scrape.content
    soup = BeautifulSoup(page, 'html.parser')
    nar = soup.find_all('div',{'class': "narrow"})
    posts = []
    for i in range(len(nar)):
        post = nar[i].text
        if len(post) > 20:
            posts.append(post)
    return posts


def get_prediction(post, loaded_class):
    pred = []
    for text in post:
        features = dict([(word, True) for word in text.split()])
        probdist = loaded_class.prob_classify(features)
        pred_sentiment = probdist.max()
        if pred_sentiment == 'Positive':
            pred.append(1)
        else:
            pred.append(0)
    print(pred)
    avg_pred = round(sum(pred)/len(pred))
    if avg_pred == 1:
        return "Positive"
    else:
        return 'Negative'


# Initialize the app
APP = Flask(__name__)

'''HTML GUI '''

# Render the home page
@APP.route('/')
def home():
    '''Display of web app homepage'''
    return render_template('index.html')

# render the new_user_recommend page
@APP.route('/company_search')
def company_find():
    '''Display of result of search'''
    return render_template('company_find.html')


# render the new user recommend page
@APP.route('/search', methods=['POST'])
def search_company():
    '''Function that accepts the company name displays search result
    for Web App Testing'''
    # get the values from the form
    try:
        search_query = [x for x in request.form.values()]
        result = search(search_query[0])
        if isinstance(result, pd.DataFrame):
            result = result.values.tolist()
            result_list = []
            for row in result:
                row = ', '.join(row)
                result_list.append(row)
            # result_list = ' \n '.join(result_list)
        else:
            result_list = [result]
        post = scrape(search_query[0])
        prediction = get_prediction(post, classifier)
        prediction_text = [f'Sentiment of Nairaland search are mostly {prediction}']
        result_list.append(prediction_text)
        return render_template('search.html', prediction_text=result_list)
    except KeyError:
        return render_template('search.html', prediction_text=[["company does not exist"]])


# run the app
if __name__ == "__main__":
    APP.run(debug=True)
