#!/usr/bin/env python
# coding: utf-8

# ## Code Without Modularization

# In[4]:


def add(a, b):
    addresult = a+b
    return addresult

def sub(a, b):
    subresult = a-b
    return subresult

Add = add(5, 4)
print(Add)

Sub = sub(5, 4)
print(Sub)


# ## Code With Modularization

# In[3]:


import addition
import substraction

Addition = addition.add(5, 4)
Substraction = substraction.sub(5, 4)

print(Addition)
print(Substraction)


# In[ ]:




