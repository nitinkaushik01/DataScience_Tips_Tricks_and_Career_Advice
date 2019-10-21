#!/usr/bin/env python
# coding: utf-8

# ### Pass the variables from one notebook to another using Magic Command : %store

# In[1]:


a = 1
b = 2
Notebook_1_Divide_variable = a/b
Notebook_1_Divide_variable


# In[2]:


get_ipython().run_line_magic('store', 'Notebook_1_Divide_variable')


# ### List out all the Global Variables using Magic command : %who

# In[3]:


a, b, c = "Hello", [1,2,3], 5


# In[4]:


get_ipython().run_line_magic('who', '')


# ### Calculate the time taken by a function, command or code snippet using Magic command : %%time

# In[8]:


get_ipython().run_cell_magic('time', '', 'Number = int(input("Please Enter any Number: "))\n\nSum = 0\nwhile(Number > 0):\n    Reminder = Number % 10\n    Sum = Sum + Reminder\n    Number = Number //10\n\nprint("\\n Sum of the digits of Given Number = %d" %Sum)')


# ### Write the content of a Jupyter Cell to a file using Magic command : %%writefile

# In[7]:


get_ipython().run_cell_magic('writefile', 'number_addition.py', 'def add_numbers(a, b):\n    if a < 10 and b < 10:\n        return 0\n    else:\n        c = a + b\n        return c')


# In[5]:


from number_addition import add_numbers as add


# In[9]:


add(1, 2)


# ### Colorful Formatting to Highlight any cell

# <div class = "alert alert-block alert-danger">
#     This cell Highlights any Markdown which needs <b>ATTTENTION!</b>
# </div>

# <div class="alert alert-block alert-success">
#     This cell Highlights any Markdown which gives <b>GO AHEAD!</b>
# </div>

# <div class="alert alert-block alert-info">
#     This cell is just for <b>INFORMATIONAL</b> purpose
# </div>

# ### Print both head() and tail() of a dataframe in the same cell

# In[15]:


import pandas as pd 

#Read a csv file
csv_df = pd.read_csv("Mall_Customers.csv")
csv_df.head()
csv_df.tail() 


# In[17]:


import pandas as pd 

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

#Read a csv file
csv_df = pd.read_csv("Mall_Customers.csv")
csv_df.head()
csv_df.tail()


# In[ ]:




