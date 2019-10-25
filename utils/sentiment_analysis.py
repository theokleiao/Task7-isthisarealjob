import joblib


def extract_features(word_list):
    return dict([(word, True) for word in word_list])


def get_predictions(input_text, classifier):
    """
    Generate sentiment analysis of a given text
    :param input_text: str;
    :param classifier: model
    :return: predicted sentiment, positive or negative
    """
    prob_dist = classifier.prob_classify(extract_features(input_text.split()))
    pred_sentiment = prob_dist.max()
    print("Predicted sentiment:", pred_sentiment)
    print("Probability:", round(prob_dist.prob(pred_sentiment), 2))
    return pred_sentiment


filename = "data/classifier.sav"
loaded_class = joblib.load(filename)

text = 'very bad company, did not pay us on time,' \
       ' very hostile environment, didnt enjoy my time there one bit, terrible experience'
get_predictions(text, loaded_class)
