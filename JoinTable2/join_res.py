import time
import pandas as pd
time1= time.time()
final_idcluster = pd.read_csv('/final_idcluster.csv',encoding='utf-8')
time2=time.time()
pd.set_option('display.max_columns',None)
print(len(final_idcluster)) #10072397
print('time1 s*************:',time2-time1)
df2 = pd.read_csv('d:/resdf21.csv',encoding='utf-8')
time3=time.time()
print('time2 s*************:',time3-time2)
print(len(df2))
import numpy as np
print(len(np.unique(df2.ids)))
# df2=df2.drop_duplicates()
res = pd.merge(final_idcluster,df2,how='left')
time4=time.time()
print('time3 s*************:',time4-time3)
print('res:',len(res))
res=res.drop_duplicates()
res.to_csv('d:/final_with_url_nodeid2.csv',index=None)
time5=time.time()
print('time4 s*************:',time5-time4)
# tt1= pd.read_csv('d:/final_with_url_nodeid.csv',encoding='utf-8')
# print(tt1.head(2))
# print(len(tt1)) #16045022
# time5=time.time()
# print('time4 s*************:',time5-time1)
