#!/usr/bin/env python
# coding: utf-8

# In[1]:


# load modules and get a data set
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('diamonds')  # load data
df = data.drop(['x', 'y', 'z'], axis=1)  # drop cols for readability


# In[3]:


df.head(10)


# In[13]:


# create the plot, init fig and ax

fig, ax = plt.subplots()
ax = sns.scatterplot(data=df, x='carat', y='price', hue='color', alpha=0.5)

plt.close()  # prevent plotting in the cell


# ![Basic Plot of the Diamonds Dataset](../source/images/03_csr_axislabels_01.png)

# See below for the implementations of these improvments and the final plot!

# In[15]:


# create the plot, init fig and ax
fig2, ax = plt.subplots()
ax = sns.scatterplot(data=df, x='carat', y='price', hue='color', alpha=0.5)

# axis labels
ax.set(xlabel='Mass in Carats', ylabel='Price in Dollars')  

# color labels and changes to the legend
labels_color = ['D (best)', 'E', 'F', 'G', 'H', 'I', 'J (worst)']
plt.legend(title='Color', loc='lower right', labels=labels_color) 

# set a title
plt.title("Diamonds Charateristics and their Price")

plt.close()  # prevent plotting in the cell

