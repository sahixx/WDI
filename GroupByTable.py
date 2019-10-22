
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


JoinTable = pd.read_csv(r'\final_idcluster.csv', encoding='utf-8')


# In[6]:


len(JoinTable)


# In[8]:


JoinTable.head(2)


# In[9]:


JoinTable.columns


# In[18]:


tmp = JoinTable.groupby('predictedLabel')['ids'].count()


# In[19]:


tmp


# In[32]:


id = JoinTable.groupby('predictedLabel')['ids'].size()


# In[33]:


id


# In[44]:


type(id)


# In[34]:


tmp.to_csv(r'\number of clusters per category')


# In[35]:


tmp = JoinTable.groupby('predictedLabel').sum()


# In[36]:


del tmp['ids']


# In[37]:


tmp


# In[45]:


type(tmp)


# In[53]:


tmp['id']=id


# In[54]:


tmp


# In[55]:


tmp.to_csv(r'C:\Users\hechen\Desktop\StatisticsSample')

