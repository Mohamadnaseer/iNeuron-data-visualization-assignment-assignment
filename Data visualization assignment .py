#!/usr/bin/env python
# coding: utf-8

# # Datisualization assignment 
In this assignment students have to transform iris data into 3 dimensions
and plot a 3d chart with transformed dimensions and colour each data
point with specific class.
Hint:
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import datasets
# In[11]:


import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
from sklearn.decomposition import PCA as P 
from sklearn import datasets 
import seaborn as sns


# In[12]:


Data = sns.load_dataset('iris')
Data


# In[15]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
Data.species = le.fit_transform(Data.species)
Data


# In[17]:


ax = plt.axes(projection='3d')
xline = Data["sepal_length"]
yline = Data["sepal_width"]
zline = Data["petal_length"]


# In[18]:


ax = plt.axes(projection='3d')
ax.scatter3D(xline, yline, zline,c =Data["petal_width"] ,cmap='viridis', linewidth=0.5)
ax.set_xlabel('sepal_length' , fontsize = 12.5)
ax.set_ylabel("sepal_width", fontsize = 12.5)
ax.set_zlabel('petal_length', fontsize = 12.5)

