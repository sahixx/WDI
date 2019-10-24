
# -*- coding: utf-8 -*-
import os
import json

os.chdir('D:\BaiduNetdiskDownload')
filename1 = 'specTablesConsistent'
# filename1 = 'offers_english.json'




def readInChunks(fileObj, chunkSize=4096):
    """
    Lazy function to read a file piece by piece.
    Default chunk size: 4kB.
    """
    while 1:
        data = fileObj.read(chunkSize)
        if not data:
            break
        yield data


#####################处理 url -special keyvalues
urls = []
kvs=[]
f = open(filename1,encoding='utf-8')
i=0
last_c = ''
for chuck in readInChunks(f):
    i+=1
    #do_something(chunk)
    #chuck=chuck.replace('}}\n{','}},\n{')
    # print(i,chuck)
    chuck =last_c+chuck
    chuck1 = chuck.split('\n')
    for c in chuck1:
        if c.endswith('}}') and c.startswith('{'):
            dic = json.loads(c)
            print(i,dic)
            urls.append(dic['url'])
            kvs.append(dic['keyValuePairs'])
            last_c=''
        else:
            last_c=c
f.close()

import pandas as pd
df=pd.DataFrame({'url':urls,'kv':kvs})

df.to_csv('d:/resdf.csv',index=None)


df.head(3)


#####################处理 url -nodeID --cluster_id
filename2='offers_consWgs_english.json'
urls2 = []
ids=[]
nodeIDs=[]
f1 = open(filename2,encoding='utf-8')
i=0
last_c = ''
for chuck in readInChunks(f1):
    i+=1
    #do_something(chunk)
    #chuck=chuck.replace('}}\n{','}},\n{')
    # print(i,chuck)
    chuck =last_c+chuck
    chuck1 = chuck.split('\n')
    for c in chuck1:
        if c.endswith('}]}') and c.startswith('{'):
            dic = json.loads(c)
            print(i,dic)
            urls2.append(dic['url'])
            ids.append(dic['cluster_id'])
            nodeIDs.append(dic['nodeID'])
            last_c=''
        else:
            last_c=c
f1.close()

import pandas as pd
df2=pd.DataFrame({'url':urls2,'ids':ids,'nodeID':nodeIDs})

df2.head(3)

df2.to_csv('d:/resdf21.csv',index=None)
#df=pd.read_csv('resdf.csv',encoding='utf-8')
# df.head(2)

df['url']=df['url'].replace('.html','')
df2['url']=df2['url'].replace('.html','')

new_df = pd.merge(df2,df,how='left')

new_df.head(3)
new_df.to_csv('mergeurl_id_kv.csv',index=None)




import ast
import json,math
import pandas as pd
import numpy as np
#new_df=pd.read_csv('mergeurl_id_kv.csv',encoding='utf-8')
idcluster = pd.read_csv('categories_offers_en_clusters.csv',encoding='utf-8')
idcluster.head(3)
new_df.head(3)
idcluster.columns = ['predictedLabel','ids']

# new_df1 = new_df[['ids','kv']]
# new_df1['nkv'] = 0

# newdf_dict = {k:v for k,v in zip(new_df['ids'],[new_df['url'],new_df['nodeIDs'],new_df['kv']])}
newdf_dict = {k:v for k,v in zip(new_df['ids'],zip(new_df['url'],new_df['nodeID'],new_df['kv']))}

# id=idcluster.ids[0]
# newdf_dict[id]

res = []
res1 = []
urls = []
nodeIDs = []
i=0
for id in idcluster.ids:
    i+=1
    if id in newdf_dict.keys():
        res.append(1)
        tmp = newdf_dict[id]
        url =tmp[0]
        nodeID =tmp[1]
        kv=tmp[2]
        urls.append(url)
        nodeIDs.append(nodeID)
        if str(kv)=='nan':
            res1.append(0)
        else:
            tmp2 = ast.literal_eval(kv)
            res1.append(len(tmp2))
            print(i,id,url,nodeID,len(tmp2))
    else:
        res.append(0)
        urls.append(0)
        nodeIDs.append(0)
        res1.append(0)
        #print(i,id,0,0)


idcluster['urls'] = urls
idcluster['nodeIDs'] = nodeIDs
idcluster['spe'] = res
idcluster['nkv'] = res1
idcluster.head(3)
idcluster.to_csv('final_idcluster.csv',index=None)
len(idcluster)


import numpy as np
import pandas as pd
idcluster=pd.read_csv('final_idcluster.csv',encoding='utf-8')
len(idcluster)
idcluster.head(2)

idcluster.columns
tmp = idcluster[['predictedLabel','spe','kv']].groupby('predictedLabel').sum()
print(tmp.head(3))
del tmp['ids']

tmp.to_csv('final_groupby.csv')
len(tmp)

len(np.unique(idcluster.predictedLabel))
