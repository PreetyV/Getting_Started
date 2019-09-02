#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[15]:


X = np.arange(0,2*np.pi,0.1)
Y = np.sin(X)
Z = np.cos(X)


# In[16]:


plt.plot(X,Y,X,Z)
plt.show()


# In[ ]:




