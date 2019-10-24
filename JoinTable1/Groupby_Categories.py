import pandas as pd
import csv

data = pd.read_csv('/Users/danielkhan/Downloads/count.csv')
#data.drop('specTableContent', axis=1)
fourcoldata = data[['predictedLabel', 'cluster_id', 'kvp_count', 'hasSpecTable', 'language_count']]
grouper = fourcoldata.groupby('predictedLabel', as_index=False)
res = grouper.count()
res['hasSpecTable'] = grouper.sum()['hasSpecTable']
res['kvp_count'] = grouper.sum()['kvp_count']
res['language_count'] = grouper.sum()['language_count']

res.to_csv('groupby2.csv', index=False)

