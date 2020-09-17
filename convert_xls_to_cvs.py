import pandas as pd

data_xls = pd.read_excel(
    'corpus/Tweets_Masterchef.xlsx'
)
data_xls.to_csv('corpus/Tweets_Masterchef.csv', encoding='utf-8')