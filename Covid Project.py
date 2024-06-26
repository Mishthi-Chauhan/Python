#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd


# In[19]:


url="https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv"
c=pd.read_csv(url)


# In[20]:


c


# In[21]:


row_count = len(c)


# In[22]:


row_count


# In[23]:


row_count = c. shape[0]


# In[24]:


row_count


# In[25]:


cols = len(c.axes[1]) 


# In[26]:


cols


# In[27]:


c.describe()


# In[28]:


c.dtypes


# In[29]:


c.describe(include="float64")


# In[30]:


c.info()


# In[31]:


c.describe(include="object")


# In[32]:


c["location"].nunique()


# In[33]:


c["location"].value_counts()


# In[34]:


c.groupby('Type').agg(Min_cases=('tatal_cases', 'min'),
                              Average=('total_cases', 'mean'),
                              Max_cases=('total_cases', 'max')).reset_index()


# In[35]:


c = c.dropna(subset=['continent'])


# In[36]:


c


# In[37]:


c["continent"].value_counts(). max()


# In[38]:


counts = c.value_counts()


# In[39]:


counts


# In[40]:


max_value= c["total_cases"].max()


# In[41]:


print(max_value)


# In[42]:


c_mean=c["total_cases"].mean()


# In[43]:


print(c_mean)


# In[44]:


c.total_cases.quantile(0.25)


# In[45]:


c.total_cases.quantile(0.5)


# In[46]:


c.total_cases.quantile(0.75)


# In[47]:


c.loc[c.groupby(['continent'] )['human_development_index'] .idxmax()]


# In[48]:


col = "human_development_index"
max_x = c.loc[c[col].idxmax()]
print ( col, max_x)


# In[49]:


max_value1= c["human_development_index"].max()


# In[50]:


print(max_value1)


# In[51]:


col1 = "gdp_per_capita"
min_x = c.loc[c[col1].idxmin()]
print ( col1, min_x)


# In[52]:


min_value= c["gdp_per_capita"].min()


# In[53]:


print(min_value)


# In[54]:


selected_columns = ['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index']
filtered_c = c[selected_columns]
print(filtered_c)


# In[55]:


filtered_c


# In[56]:


filtered_c.duplicated().sum()


# In[57]:


filtered_c.drop_duplicates


# In[58]:


filtered_c


# In[59]:


filtered_c.isnull().sum()


# In[60]:


column_to_check = 'continent'
c_cleaned = filtered_c.dropna(subset=[column_to_check])


# In[61]:


c_cleaned


# In[62]:


c_filled = c_cleaned.fillna(0)


# In[63]:


c_filled


# In[64]:


c_filled['date'] = pd.to_datetime(c_filled['date'])


# In[65]:


c_filled


# In[66]:


c_filled['month']=c_filled['date'].dt.month


# In[67]:


c_filled


# In[68]:


max_values_by_continent = c_filled.groupby('continent').max().reset_index()


# In[69]:


max_values_by_continent


# In[70]:


c_groupby = c_filled.groupby('continent').max().reset_index()


# In[71]:


c_groupby


# In[72]:


c_filled['total_deaths_to_total_cases'] = c_filled['total_deaths'] / c_filled['total_cases']


# In[73]:


c_filled


# In[74]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[75]:


plt.figure(figsize=(10,7))
sns.histplot(c_filled["gdp_per_capita"])


# In[ ]:


sns.catplot(x='total_cases', y='gdp_per_capita', data= c_filled, kind="point")


# In[ ]:


sns.pairplot(c_groupby, hue='continent')
plt.suptitle('Pair Plot of c_groupby Dataset', y=1.02)
plt.show()


# In[ ]:


sns.catplot(x='continent', y='total_cases', data=c_filled, kind='bar')
plt.title('Bar Plot of Total Cases by Continent')
plt.xlabel('Continent')
plt.ylabel('Total Cases')
plt.show()


# In[ ]:


c_groupby.to_csv('c_groupby_data.csv', index=False)


# In[ ]:




