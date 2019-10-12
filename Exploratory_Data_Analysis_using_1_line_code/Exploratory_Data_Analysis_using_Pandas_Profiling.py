#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install pandas-profiling')

#One can also run the conda forge command below to install the same package
#conda install -c conda-forge pandas-profiling


# In[1]:


# import necessary packages
import pandas as pd
import pandas_profiling
import numpy as np


# In[3]:


pandas_profiling.ProfileReport(pd.read_csv('Titanic_Dataset.csv'))


# In[ ]:




