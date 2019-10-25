import pandas as pd
from difflib import get_close_matches

cac_db = pd.read_csv(r'data\cac_db.csv')


def search(word):
    word = word.upper()

    def start(x):
        if x.startswith(word):
            return True
        else:
            return False

    if len(cac_db[cac_db['COMPANY NAME'].apply(start)]) > 0:
        return cac_db[cac_db['COMPANY NAME'].apply(start)]
    elif len(get_close_matches(word, cac_db['COMPANY NAME'], 5, cutoff=0.7)) > 0:
        return get_close_matches(word, cac_db['COMPANY NAME'], 5, cutoff=0.7)
    else:
        return "Not in CAC database"


print(search("hng"))
