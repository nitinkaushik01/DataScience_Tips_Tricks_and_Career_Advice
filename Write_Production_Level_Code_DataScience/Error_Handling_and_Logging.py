#!/usr/bin/env python
# coding: utf-8

# ## Error Handling

# In[3]:


def div(a, b):
    divresult = a/b
    return divresult

Div = div(4, 0)
print(Div)


# In[16]:


def div(a, b):
    try:
        divresult = a/b
        return divresult
    except:
        print("Second argument value can't be Zero")
        

Div = div(4, 0)
print(Div)


# ## Enable Logging

# In[17]:


import logging

logging.basicConfig(filename='warning.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')


# In[ ]:




