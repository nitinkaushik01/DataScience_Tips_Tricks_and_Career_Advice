#!/usr/bin/env python
# coding: utf-8

# # Run Shell Commands

# In[1]:


get_ipython().system('pwd')


# # Auto-Complete Feature

# In[ ]:


#Type something to see auto-completion in action
import numpy


# # Table of Content Feature

# ## Import important libraries

# In[7]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
import os


# ## Change working directory

# In[7]:


os.chdir('F:')


# ### Read .csv file

# In[8]:


datafile = pd.read_csv('Student_Grades_Data.csv')
datafile.head()


# ### Describe shape of the Data

# In[9]:


datafile.shape


# # Jupyter Notebook Shortcuts

# ## List of all the shortcuts

# In[10]:


#H: show all the shortcuts available in Jupyter Notebook
#A: insert a new cell above
#B: insert a new cell below
#Shift + Up/Down Arrow: select multiple notebook cells at the same time
#Ctrl + Enter: to run all the selected cells
#M: change the type of cell to Markdown
#Y: change the type of cell to Code
#X: cut the selected cells
#Z: undo the deletion of a cell
#Space: scroll notebook down
#Shift + Space: scroll notebook up
#Shift + Enter: run the current cell and move the next one
#Ctrl + s: save notebook


# In[11]:


# Demonstrate Esc+A and Esc+B


# In[2]:


# Demonstrate Esc+Shift+Up/Down Arrow Keys as well as Ctrl+Enter


# In[3]:


a=1


# In[4]:


b=2


# In[5]:


c=a+b


# In[6]:


c


# In[ ]:


# Demonstrate Esc+M and Esc+Y


# In[14]:


# Demonstrate Esc+X and Esc+Z


# In[15]:


# Demonstrate Esc+Space and Esc+Shift+Space


# In[16]:


# Demonstrate Shift+Enter


# In[ ]:


# Demonstrate Ctrl+S

