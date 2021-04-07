#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
import math

# In[2]:


lst = []
for i in range(0, 300):
    lst.append((np.random.randint(0, 100)))
print(lst)

# In[16]:


del cluster

# In[17]:


centers = [40, 60, 90]
cluster = [[], [], []]


# In[18]:


def euclidean_distance(centers, data):
    distance0 = math.sqrt((data - centers[0]) * (data - centers[0]))
    distance1 = math.sqrt((data - centers[1]) * (data - centers[1]))
    distance2 = math.sqrt((data - centers[2]) * (data - centers[2]))
    return distance0, distance1, distance2


# In[19]:


for element in lst:
    distance0, distance1, distance2 = euclidean_distance(centers, element)

    if distance0 < distance1 and distance0 < distance2:
        cluster[0].append(element)
        centers[0] = (centers[0] + element) / 2
        print("center 0:", (centers[0] + element) / 2)

    elif distance1 < distance0 and distance1 < distance2:
        cluster[1].append(element)
        centers[1] = (centers[1] + element) / 2
        print("center 1:", (centers[1] + element) / 2)

    elif distance2 < distance0 and distance2 < distance1:
        cluster[2].append(element)
        centers[2] = (centers[2] + element) / 2
        print("center 2:", (centers[2] + element) / 2)

# In[20]:


len(cluster[0]) + len(cluster[1]) + len(cluster[2])

# In[21]:


centers

# In[23]:


for i in cluster:
    print(sorted(i), "\n")
    print(len(i))

# In[ ]:



