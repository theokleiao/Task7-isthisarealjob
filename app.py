#''' Deploy user recomender model using flask framework'''

# Import Relevant Modules
try:
    import pickle
    import joblib
    from flask import request, render_template
    import pandas as pd

except ImportError as i_error:
    print(i_error)

# Load the datasets needed for deployment
CAC_DB = pd.read_csv('used_data/cac_db.csv')
CAC_DB['name'] = CAC_DB.name.str.lower()

# load the model from disk
MODEL = joblib.load('cac.py')

def search(company_name):
    '''Declaring a function that would use our model to fetch users
    similar to a given user based on user_bio'''
    try:
       
        # Return the company
        return CAC_DB['name'].iloc[users_index]
    except KeyError:
        return 'Enter a valid company name'
    except IndexError:
        return 'This company doesnt exist'

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
    return render_template('company_search.html')


# render the new user recommend page
@APP.route('/search', methods=['POST'])
def company_find():
    '''Function that accepts the company name displays search result
    for Web App Testing'''
    # get the values from the form
    try:
        search = [x for x in request.form.values()]
        for name in company:
            name_of_user = name.lower()

        # recommend
        company = MODEL.recommend((CAC_DB[CAC_DB.name == Company name]['name']).index[0])
        
        Company_search= []
        for i_d in popular_users['user_id']:
            Company_search.append(CAC_DB.iloc[i_d, 0])
        return render_template('cac_search.html', prediction_text=recommended_users)
    except KeyError:
        return render_template('cac_search.html', prediction_text=["company does not exist"])


# run the app
if __name__ == "__main__":
    APP.run(debug=True)
