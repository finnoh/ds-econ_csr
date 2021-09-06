#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing

dict_data = fetch_california_housing()

list_names = dict_data.feature_names
list_names.extend(dict_data.target_names)

data = np.concatenate([dict_data.data, dict_data.target.reshape(-1,1)], axis=1)
df = pd.DataFrame(data=data, columns=list_names)

