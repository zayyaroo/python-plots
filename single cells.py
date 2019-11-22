
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


Livecells = pd.read_csv('Objects_Population - Life Stain.txt',delimiter="\t")


# In[3]:


Livecells.head()


# In[4]:


Livecells = Livecells.drop(Livecells.columns[[2,3,4,6,7,8,9,10,11,12,16]],axis = 1)


# In[5]:


Livecells['Row'] = Livecells['Row'].apply(str)
Livecells['Column'] = Livecells['Column'].apply(str)


# In[6]:


Livecells['Tm'] = Livecells['Row'].replace({'2':'Gox','3':'Empty','4':'Gox','5':'Empty','6':'Gox','7':'Empty'})


# In[7]:


Livecells['Glu'] = Livecells['Row'].replace({'2':'0.17','3':'0.17','4':'0.8','5':'0.8','6':'1.4','7':'1.4'})


# In[8]:


Livecells['Vesciles'] = Livecells['Column'].replace({'2':'conc1','3':'conc1','4':'conc1','5':'conc2','6':'conc2','7':'conc2','8':'conc3','9':'conc3','10':'conc3'})


# In[9]:


Livecells.head()


# In[10]:


lowglu_c1 = Livecells [(Livecells['Glu']== '0.17') & (Livecells['Vesciles']== 'conc1')]
highglu_c1 = Livecells[(Livecells['Glu']== '1.4')&(Livecells['Vesciles']== 'conc1')]


# In[11]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[37]:


deadcells['Row']=deadcells['Row'].apply(str)
deadcells['Column']=deadcells['Column'].apply(str)
deadcells['Tm'] = deadcells['Row'].replace({'2':'Gox','3':'Empty','4':'Gox','5':'Empty','6':'Gox','7':'Empty'})
deadcells['Glu'] = deadcells['Row'].replace({'2':'0.17','3':'0.17','4':'0.8','5':'0.8','6':'1.4','7':'1.4'})
deadcells['Ves'] = deadcells['Column'].replace({'2':'conc1','3':'conc1','4':'conc1','5':'conc2','6':'conc2','7':'conc2','8':'conc3','9':'conc3','10':'conc3'})


# In[38]:


deadcells.head()


# In[40]:


deadcells.describe()


# In[60]:


g = sns.catplot(x='Glu',data=deadcells,hue='Tm',col='Ves',kind='count',aspect=.6)
(g.set_axis_labels("Glucose conc","#dead cells")
.set_titles("{conc1}{highest_conc}"))


# In[55]:


get_ipython().run_line_magic('pinfo', 'sns.catplot')

