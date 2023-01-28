#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python code to find smallest K-digit 
# number divisible by X
 
def answer(X, K):
     
    # Computing MAX
    MIN = pow(10, K-1)
     
    if(MIN%X == 0):
        return (MIN)
     
    else:
        return ((MIN + X) - ((MIN + X) % X))
     
 
X = 83;
K = 5;
 
print(answer(X, K));


# In[ ]:




