#!/usr/bin/env python
# coding: utf-8

# In[8]:


# load modules and get a data set
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000)  # generate a class. problem


# The first step in our mini "pipeline" is to split the data set into training and test set. This splitting of the data is important, to prevent overfitting and have an evaluation of the model which reprensents its real-life performance more closely. We can do this in a neat way with sklearn's [`model_selection.train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split).

# In[14]:


from sklearn.model_selection import train_test_split

# create train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0)


# In[15]:


# train the model on the training data
from sklearn.linear_model import LogisticRegression

# initialize the model with fixed hyperparameters - see doc!
model = LogisticRegression(penalty="l2", C=1.0, random_state=0)

# fit the model to the data
model.fit(X_train, y_train)

# make a prediction on unseen data i.e. the test set
prediction = model.predict(X_test)


# In[18]:


from sklearn.metrics import accuracy_score
# calculate the performance as the accuracy score
print(f'The models accuracy is: {accuracy_score(y_test, prediction)}')


# ## Getting More Complex: Adding Hyperparameter-Tuning

# In[19]:


from sklearn.model_selection import train_test_split

# create train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=1)


# In[53]:


from scipy.stats import norm

# initilaize RandomSearch
dist_param = {'max_depth':[1, 5, 10, 20], 'criterion':['gini', 'entropy']}


# In[55]:


# train the model on the training data
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import RandomizedSearchCV

model = DecisionTreeClassifier(random_state=0)
rcv = RandomizedSearchCV(model, dist_param, random_state=1, verbose=3, n_iter=5, 
                         cv=3)

# fit the model to the data
rcv.fit(X_train, y_train)

# make a prediction on unseen data i.e. the test set
prediction = rcv.predict(X_test)


# In[56]:


from sklearn.metrics import accuracy_score
# calculate the performance as the accuracy score
print(f'The models accuracy is: {accuracy_score(y_test, prediction)}')


# ### Using the Optimal Hyperparameters in a different Model

# In[99]:


best_params = rcv.best_params_  # get the best hyperparameters found by RS
print(best_params)


# In[97]:


from sklearn.tree import plot_tree

# plot the decision tree for better intuition
model_tree = DecisionTreeClassifier(**best_params)  # unpack the dictionary

model_tree.fit(X, y)  # fit on whole data set for the plot

# plot the decision tree with plot_tree
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (10,7.5), dpi=200)
plot_tree(model_tree, impurity=False, ax=axes, filled=True, max_depth=2,
          fontsize=12)

plt.close()


# In[98]:


fig.savefig("../source/images/05_csr_firstmlmodel_01.jpg")

