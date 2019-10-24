import re
import pandas as pd
posts = pd.read_csv('/Users/naeamakachalokwu/Documents/data/posts.csv')
posts.head()
posts.drop[('updated_at', 'created_at', 'pictures', 'deleted_at', 'verified'), axis=1, inplace=True]