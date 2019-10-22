import pandas as pd
data_csv = pd.read_csv('/Users/danielkhan/Downloads/categories_offers_en_clusters.csv')
print(data_csv.head())

data_csv.groupby('predictedLabel').size().reset_index(name='counts')
import json
from pandas.io.json import json_normalize

with open('/Users/danielkhan/Downloads/sample_offersenglish.json') as f:
    d = json.load(f)

df_json = json_normalize(d)
df_json2 = pd.DataFrame(df_json, columns=['cluster_id', 'url', 'nodeID'])

df_json2['cluster_id'] = df_json2['cluster_id'].astype(int)
df2 = df_json2
print(df2)

df3 = data_csv
print(df3)
print(type(df2))
print(type(df3))

result = pd.merge(df2, df3, on='cluster_id')

print(result)
