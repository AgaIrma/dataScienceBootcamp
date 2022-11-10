#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ex_02_create_tables.py

import sqlite3
import pandas as pd
import sqlalchemy as sq
from sqlite3 import Error


if __name__ == "__main__":
    # Connect to SQLite
    conn = sqlite3.connect('sql3.db')
    cursor = conn.cursor()
    df_station = pd.read_csv("C:/Users/aga/Downloads/clean_stations.csv")
    df_measure = pd.read_csv("C:/Users/aga/Downloads/clean_measure.csv")
    df = pd.merge(df_station,df_measure,how='inner',on='station')
    print(df.columns)
    df.to_sql('station', conn, chunksize=1000, if_exists='append')
    #df.to_sql('stations', conn, method = 'multi', if_exists='append', index=False)
    conn.commit()
    count = conn.execute("SELECT count(*) FROM station")
    print({count})
 


# In[2]:


rows = conn.execute("SELECT * FROM station LIMIT 5 ").fetchall()
for row in rows:
    print(row)


# In[ ]:





# In[ ]:




