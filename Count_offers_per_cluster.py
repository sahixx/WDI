import csv
import json
import pandas as pd

data = pd.read_csv('Final.csv')
twocoldata = data[['cluster_id', 'url']]
grouped = twocoldata.groupby('cluster_id', as_index=False)['url'].count()

df = grouped.to_csv('offers_per_cluster.csv', index=False)