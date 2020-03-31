#!/usr/bin/env python
# coding: utf-8

# <a href="https://cognitiveclass.ai"><img src = "https://ibm.box.com/shared/static/9gegpsmnsoo25ikkbl4qzlvlyjbgxs5x.png" width = 400> </a>
# 
# <h1 align=center><font size = 5>Peer-graded Assignment: Segmenting and Clustering Neighborhoods in Toronto Part 1</font></h1>

# In[46]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
print('Libraries imported.')


# ### Scrape the List of postal codes of Canada

# Had to switch the !get method, was not getting me anywhere.

# In[41]:


List_url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
source = requests.get(List_url).text


# In[47]:


canada = BeautifulSoup(source, 'xml')


# In[48]:


#dataframe will consist of three columns: PostalCode, Borough, and Neighborhood
column_names = ['Postalcode','Borough','Neighborhood']
df = pd.DataFrame(columns = column_names)


# In[49]:


# Search all the postcode, borough, neighborhood 
for tr_cell in table.find_all('tr'):
    row_data=[]
    for td_cell in tr_cell.find_all('td'):
        row_data.append(td_cell.text.strip())
    if len(row_data)==3:
        df.loc[len(df)] = row_data


# In[50]:


df.head()


# ### Cleaning the data

# In[52]:


df=df[df['Borough']!='Not assigned']


# In[60]:


df


# As we can see in the dataframe above it´s not necesary to merge rows with same postal code because the updated list have alredy done this.

# Now to fix the index.

# In[68]:


df=df.reset_index(drop=False)


# In[76]:


df.drop(columns = ['index'], inplace = True)


# In[78]:


df.head(5)


# In[79]:


df.shape

