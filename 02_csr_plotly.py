#!/usr/bin/env python
# coding: utf-8

<<<<<<< HEAD
# In[32]:
=======
# In[19]:


from IPython.display import HTML, display
display(HTML(filename='../source/first_figure.html'))


# In[21]:
>>>>>>> d72136ac96ed912ca26a15f50814f57fc9c6ed1b


import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import src.ds_econ_ploty

pio.templates.default = "ds_econ"  # ds-econ template

df = px.data.gapminder()  # load the data
df_2007 = df.query("year==2007")  # subset to the year of 2008

# specify the labels of the plot
labels = {'gdpPercap':'GDP per Capita', 
          'lifeExp':'Life Expectancy', 
          'pop':'Population',
          'continent':'Continent'}

# create the scatterplot with log-xaxis
fig = px.scatter(df_2007,
                 x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 log_x=True, size_max=60,
                 title="Gapminder",
                 labels=labels)

# safe the figure as html file
fig.write_html('../source/first_figure.html', auto_open=False)


<<<<<<< HEAD
# In[33]:
=======
# In[22]:
>>>>>>> d72136ac96ed912ca26a15f50814f57fc9c6ed1b


from IPython.display import HTML, display
display(HTML(filename='../source/first_figure.html'))

