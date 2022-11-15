#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install plotly
#!pip install cufflinks


# Pobierz dane dotyczące cen akcji KGHM oraz cen miedzi.
# 
# Stwórz dwa osobne wykresy liniowe (jeden pod drugim) – jeden niech przedstawia ceny zamknięcia KGHM, drugi niech przedstawia ceny miedzi (na podstawie kolumn "Zamknięcie").

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
import datetime as dt
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
import cufflinks as cf
import plotly.offline as pyo
import plotly.graph_objs as go
cf.go_offline()

dfk = pd.read_csv('/Users/aga/Downloads/kgh_d.csv')
dfk.columns
print(dfk.isnull().sum())




# In[ ]:





# Stwórz dwa osobne wykresy liniowe (jeden pod drugim) – jeden niech przedstawia ceny zamknięcia KGHM,
# drugi niech przedstawia ceny miedzi (na podstawie kolumn "Zamknięcie").
# 
# 

# In[3]:


dfk.iplot(kind='line',
x='Data',
y='Zamkniecie',
         	xTitle='KGHM',
yTitle='data notowania')




# In[4]:


dfm = pd.read_csv('/Users/aga/Downloads/ca_c_f_d.csv')
dfm.columns
print(dfm.isnull().sum())
dfm.iplot(kind='line',
x='Data',
y='Zamkniecie',
         	xTitle='data notowania',
yTitle='Wartosc miedzi w chwili zamkniecia')


# In[5]:


df_merge = pd.merge(dfk,dfm,how='inner',on='Data')
df_merge.columns


# In[6]:


df2 = df_merge[['Data', 'Zamkniecie_x', 'Zamkniecie_y']]
df2.rename(columns={'Zamkniecie_x':'KGHM'}, inplace=True)
df2.rename(columns={'Zamkniecie_y':'Miedz'}, inplace=True)
df2


# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')
fig = plt.figure(figsize=(12,6))
ax = fig.add_axes([0,0,1,1])

plt.title('KGHM i Miedz notowania', fontsize=15)

x = list(df2['Data'][:7])
y = list(df2['KGHM'][:7])
y2 = list(df2['Miedz'][:7])

plt.plot(x, y,label="KGHM")
plt.plot(x,y2, color = 'red', label="Miedz")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

