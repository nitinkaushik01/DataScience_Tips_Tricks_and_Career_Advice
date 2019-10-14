#!/usr/bin/env python
# coding: utf-8

# # Python Pandas equivalent SQL Queries

# In[67]:


#Import necessary libraries and load the data
import pandas as pd

customers = pd.read_csv('Mall_Customers.csv')


# ### SELECT

# In[68]:


#SQL Statement (Simple SELECT)
'''SELECT * FROM customers'''

#Pandas Equivalant
customers


# ### LIMIT

# In[11]:


#SQL Statement (SELECT with limited number of records)
'''SELECT * FROM customers LIMIT 7'''

#Pandas Equivalant
customers.head(7)


# ### SELECT...WHERE

# In[14]:


#SQL Statement (SELECT and WHERE on single condition)
'''SELECT CustomerID FROM customers WHERE Annual_Income_K_Dollars = 16'''

#Pandas Equivalant
customers[customers.Annual_Income_K_Dollars == 16].CustomerID


# ### SELECT...WHERE (Multiple conditions, All columns)

# In[16]:


#SQL Statement (SELECT and WHERE on multiple conditions such that all the columns will be selected)
'''SELECT * FROM customers WHERE Annual_Income_K_Dollars = 16 AND Spending_Score_1_to_100 = 6'''

#Pandas Equivalant
customers[(customers.Annual_Income_K_Dollars == 16) & (customers.Spending_Score_1_to_100 == 6)]


# ### SELECT...WHERE(Multiple consitions, Subset of columns)

# In[17]:


#SQL Statement (SELECT and WHERE on multiple conditions such that subset of columns will be selected)
'''SELECT Genre, Age, Spending_Score_1_to_100 FROM customers WHERE Annual_Income_K_Dollars = 16 AND 
Spending_Score_1_to_100 = 6'''

#Pandas Equivalant
customers[(customers.Annual_Income_K_Dollars == 16) & (customers.Spending_Score_1_to_100 == 6)][['Genre', 'Age', 'Spending_Score_1_to_100']]


# ### AGGREGATE

# In[18]:


#SQL Statement (Operation using AGGREGATE functions like MEAN, MIN and MAX)
'''SELECT mean(Age), max(Age), min(Age) FROM customers'''

#Pandas Equivalant
customers.agg({'Age': ['mean', 'max', 'min']})


# ### DISTINCT

# In[19]:


#SQL Statement (Finding distinct values of a column)
'''SELECT DISTINCT Annual_Income_K_Dollars FROM customers'''

#Pandas Equivalant
customers.Annual_Income_K_Dollars.unique()


# ### ORDERBY (Ascending Order)

# In[20]:


#SQL Statement (Filtering on Genre called Female & Ordering By Spending_Score_1_to_100)
'''SELECT * FROM customers WHERE Genre = "Female" ORDER BY Spending_Score_1_to_100'''

#Pandas Equivalant
customers[customers.Genre == 'Female'].sort_values('Spending_Score_1_to_100')


# ### ORDERBY (Descending Order)

# In[21]:


#SQL Statement (Filtering on Genre called Female & Ordering By Spending_Score_1_to_100 in DESCENDING order)
'''SELECT * FROM customers WHERE Genre = "Female" ORDER BY Spending_Score_1_to_100 DESC'''

#Pandas Equivalant
customers[customers.Genre == 'Female'].sort_values('Spending_Score_1_to_100', ascending=False)


# ### GROUPBY (Count)

# In[6]:


#SQL Statement (Grouping by Genre & Age and counting each occurence of it)
'''SELECT Genre, Age, count(*) FROM customers GROUPBY Genre, Age'''

#Pandas Equivalant
customers.groupby(['Genre', 'Age']).size().to_frame('Count').reset_index()


# ### GROUPBY (Count and Descending order on a column)

# In[56]:


# SQL Statement (Grouping by Genre & Age and counting each occurence of it such that Age values are sorted in descending order)
'''SELECT Genre, Age, count(*) FROM customers GROUPBY Genre, Age ORDER BY Age DESC'''

#Pandas Equivalant
customers.groupby(['Genre', 'Age']).size().to_frame('Count').reset_index().sort_values('Age', ascending = False)


# ### HAVING

# In[7]:


#SQL Statement (Additional filter on Grouped Data by making use of HAVING)
'''SELECT Age, count(*) FROM customers GROUPBY Age HAVING count(*) < 3'''

#Pandas Equivalant
customers.groupby('Age').filter(lambda x: len(x) < 3).groupby('Age').size()


# ### IN

# In[48]:


#SQL Statement (Filter records based on values which are available in the given list )
'''SELECT * FROM customers WHERE Age IN (10, 20, 30)'''

#Pandas Equivalant
customers[customers.Age.isin([10,20,30])]


# ### NOT IN

# In[49]:


#SQL Statement (Filter records based on values which are NOT available in the given list)
'''SELECT * FROM customers WHERE Age NOT IN (10, 20, 30)'''

#Pandas Equivalant
customers[~customers.Age.isin([10,20,30])]


# ### Top N Observations

# In[8]:


#SQL Statement (Identify Top 10 records)
'''SELECT * FROM customers ORDER BY Spending_Score_1_to_100 DESC LIMIT 10'''

#Pandas Equivalant
customers.nlargest(10, columns='Spending_Score_1_to_100')


# ### Top N Observations  with Offset

# In[11]:


#SQL Statement (Identify Next Top 10 records)
'''SELECT * FROM customers ORDER BY Spending_Score_1_to_100 DESC LIMIT 10 OFFSET 10'''

#Pandas Equivalant
customers.nlargest(20, columns='Spending_Score_1_to_100').tail(10)


# ### JOIN

# In[13]:


transactions = pd.read_csv('Mall_Customers_Transactions.csv')

#SQL Statement (Join two Tables)
'''SELECT * FROM customers c JOIN transactions t ON c.CustomerID = t.CustID WHERE c.Genre = "Female" '''

#Pandas Equivalant
customers.merge(transactions[customers.Genre == 'Female'], left_on='CustomerID', right_on='CustID', how='inner')


# ### UNION ALL

# In[29]:


shop_customers = pd.read_csv('Shop_Customers.csv')

#SQL Statement (Union two Tables)
'''SELECT * FROM customers WHERE Annual_Income_K_Dollars > 50 UNION ALL SELECT * FROM shop_customers < 45 '''

#Pandas Equivalant
pd.concat([customers[customers.Annual_Income_K_Dollars > 50], shop_customers[shop_customers.Annual_Income_K_Dollars < 45]])

#If wants to mimic UNION operation then just (append) chain the entire operation with drop_duplicates() method


# ### INSERT

# In[61]:


#SQL Statement (Insert a new record in the table)
'''INSERT INTO customers VALUES(401, 'Male', 50, 30, 20) '''

#Pandas Equivalant
customers = customers.append({'CustomerID':401, 'Genre':'Male', 'Age':50, 'Annual_Income_K_Dollars':30, 'Spending_Score_1_to_100':20}, ignore_index=True)
customers


# ### UPDATE

# In[78]:


#SQL Statement (Update an existing record in the table)
'''UPDATE customers SET Spending_Score_1_to_100 = 7 WHERE Spending_Score_1_to_100 = 6'''

#Pandas Equivalant
customers.loc[customers['Spending_Score_1_to_100'] == 6, 'Spending_Score_1_to_100'] = 7


# In[83]:


customers = pd.read_csv('Mall_Customers.csv')

#Currently two records with Spending_Score_1_to_100 == 6
customers[(customers.Spending_Score_1_to_100 == 6)]


# ### DELETE

# In[84]:


#SQL Statement (Delete an existing record in the table)
'''DELETE FROM customers SET WHERE Spending_Score_1_to_100 = 7'''

#Pandas Equivalant
customers.drop(customers[customers.Spending_Score_1_to_100 == 6].index)


# In[ ]:




