import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('groupby2.csv')
data_to_plot = data[['predictedLabel', 'cluster_id', 'kvp_count', 'hasSpecTable']].sort_values(by='kvp_count', ascending='False')
p = data_to_plot.set_index('predictedLabel').plot(kind='bar', title='Number of offers, k/v pairs and specification tables for each category')
p.set_xlabel('category')
p.legend(['offers', 'key-value pairs', 'specification tables'])
plt.show()
