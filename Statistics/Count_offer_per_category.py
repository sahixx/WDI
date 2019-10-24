import csv
import json
import pandas as pd

data = pd.read_csv('Final.csv')
twocoldata = data[['cluster_id', 'offers']]
grouped = twocoldata.groupby('cluster_id', as_index=False)['kvp_count'].sum()

df = grouped.to_csv('offers_per_category.csv', index=False)
