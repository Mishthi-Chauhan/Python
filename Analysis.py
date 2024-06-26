#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df1=pd.read_csv(r"C:\Users\misht\Downloads\drinks.csv")


# In[3]:


df1


# In[4]:


df1.sort_values(by="total_litres_of_pure_alcohol",ascending=False)


# # Concat

# In[6]:


Div_1=pd.DataFrame({"roll_no":[1,2,3,4,5],"First_name":["Tanish","Vaibhav","kundan","Sanjay","Sangeeta"],"Last_Name":["X","Y","Z","A","B"],"English":[10,20,30,40,34]})


# In[7]:


Div_2=pd.DataFrame({"roll_no":[7,8,9,10],"First_name":["Vai","kun","San","Sang"],"Last_Name":["Y2","Z4","A4","B8"],"Hindi":[56,34,67,12]})


# In[8]:


Div_1


# In[9]:


Div_2


# In[10]:


pd.concat([Div_1,Div_2],axis=0) #axes=0 is to merge row-wise , 1 would be for column


# In[11]:


pd.concat([Div_1,Div_2],axis=1) #column-wise


# In[12]:


Div_3=pd.DataFrame({"roll_no":[5,7,8,9,10],"First_name":["Sangeeta","Vai","kun","San","Sang"],"Last_Name":["B","Y2","Z4","A4","B8"],"Hindi":[34,56,34,67,12]})


# In[13]:


Div_3


# In[14]:


Div_1


# In[15]:


pd.concat([Div_1,Div_3],axis=0) #illogical lag rha h


# In[16]:


pd.merge(Div_1,Div_3,on=["roll_no","First_name", "Last_Name"],how="outer")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




