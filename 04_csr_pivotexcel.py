#!/usr/bin/env python
# coding: utf-8

# In[4]:


# load modules and get a data set
import pandas as pd
import seaborn as sns
import numpy as np

# specify datatypes that we want to use
dtype = {'Caretaker':str, 'Name':str, 'Animal':str, 'Food-Expenses':float}

# read in the zoo data and store in df, to prevent reloading from disk
data = pd.read_csv("animal_expenses.csv", delimiter=";", dtype=dtype)
df = data


# In[5]:


df


# In[9]:


pivot_table = pd.pivot_table(df, index=["Caretaker", "Animal"],
               values=["Food-Expenses"],
                            aggfunc=[np.sum])


# In[10]:


pivot_table


# In[ ]:


get_ipython().system('pip install openpyxl #  install openpyxl')


# In[12]:


pivot_table.to_excel("caretaker_expenses.xlsx", engine="openpyxl")


# !git subtree push --prefix=csr_repo https://github.com/finnoh/ds-econ_csr.git main 
