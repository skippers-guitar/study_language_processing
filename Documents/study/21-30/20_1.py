from pprint import pprint

import pandas as pd

df_wiki = pd.read_json('./jawiki-country.json', lines=True)

print(df_wiki[(df_wiki['title'] == 'イギリス')]['text'].values.item())