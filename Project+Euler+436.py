
# coding: utf-8

# In[32]:


import numpy as np
import pandas as pd
import matplotlib as plt
import collections


# In[ ]:


def single_game(a,b):
    
        s = np.array([0,
            np.random.uniform(high=1,low=0,size=1)])

        while sum(s) < a:
            x = np.random.uniform(1,0,1)
            s = np.append(s,x)
            if sum(s) > a:
                break
    
        while sum(s) < b:
            y = np.random.uniform(1,0,1)
            s = np.append(s,y)
            if sum(s) > b:
                break
            
        if x > y:
            return "Player 1 Wins"
        
        if y > x:
            return "Player 2 wins"


# In[44]:


single_game(1,2)


# In[45]:


def unfair_wager(a,b,r):
    def single_game(a,b):
    
        s = np.array([0,
            np.random.uniform(high=1,low=0,size=1)])

        while sum(s) < a:
            x = np.random.uniform(1,0,1)
            s = np.append(s,x)
            if sum(s) > a:
                break
    
        while sum(s) < b:
            y = np.random.uniform(1,0,1)
            s = np.append(s,y)
            if sum(s) > b:
                break
            
        if x > y:
            return "Player 1 Wins"
        if y > x:
            return "Player 2 Wins"
    
    out = map(lambda x: single_game(a,b), range(r))

    return out


# In[47]:


unfair_wager(1,2,10)


# In[48]:


def unfair_wager(a,b,r):
    def single_game(a,b):
    
        s = np.array([0,
            np.random.uniform(high=1,low=0,size=1)])

        while sum(s) < a:
            x = np.random.uniform(1,0,1)
            s = np.append(s,x)
            if sum(s) > a:
                break
    
        while sum(s) < b:
            y = np.random.uniform(1,0,1)
            s = np.append(s,y)
            if sum(s) > b:
                break
            
        if x > y:
            return "Player 1 Wins"
        if y > x:
            return "Player 2 Wins"
    
    out = map(lambda x: single_game(a,b), range(r))

    return pd.value_counts(out)


# In[49]:


unfair_wager(1,2,10)


# In[50]:


unfair_wager(1,2,1000)


# In[51]:


unfair_wager(1,3,1000)

