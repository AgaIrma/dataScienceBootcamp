#!/usr/bin/env python
# coding: utf-8

# Do wykonania zadań niezbędne będzie pobranie bazy filmów oraz bazy gatunków:
# 
# Baza filmów
# 
# Baza gatunków
# 
# Zwróć listę 10 najwyżej ocenianych filmów (vote_average), których liczba głosów (vote_count) jest większa od 3. kwartyla rozkładu liczby głosów.
# 
# Pogrupuj tabelę w taki sposób, aby otrzymać średni przychód (revenue) oraz średni budżet (budget) w danym roku dla filmów opublikowanych od 2010 (włącznie) do 2016 roku (włącznie). Następnie na tej podstawie stwórz wykres, w którym średnie przychody są wykresem kolumnowym, a średni budżet wykresem liniowym na tych samych osiach. Sformatuj odpowiednio oś X oraz oś Y. Dodaj tytuł wykresu, oraz legendę, która znajduje się w prawym górnym rogu płótna, lecz poza obszarem osi. Przykład wykresu widoczny poniżej:
# 
# image
# Baza filmów zawiera kolumnę z id gatunku (genre_id). Na tej podstawie połącz ze sobą bazę filmów z bazą gatunków, tak aby w bazie filmów można było odczytać nazwę gatunku filmu.
# 
# Jaki gatunek filmu z bazy pojawia się w niej najczęściej? Ile filmów tego gatunku znajduje się w bazie?
# 
# Filmy, którego gatunku trwają średnio najdłużej (runtime)?
# 
# Stwórz histogram czasu trwania filmów z gatunku, który cechuje się największym średnim czasem trwania.
# 
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

movies = pd.read_csv('/Users/aga/Downloads/tmdb_movies.csv')
columns_names = movies.columns
#print(columns_names)
movies_cleaned = movies[ ['budget', 'id', 
       'original_title', 'popularity', 'release_date', 'revenue',
       'runtime', 'status', 'title', 'vote_average', 'vote_count',
       'genre_id']]
#print(movies_cleaned.sample)

genres = pd.read_csv('/Users/aga/Downloads/tmdb_genres.csv')
genres.rename(columns={'Unnamed: 0':'genre_id'}, inplace=True)
genres_columns = genres.columns
#print(genres.sample)
#Baza filmów zawiera kolumnę z id gatunku (genre_id). 
#Na tej podstawie połącz ze sobą bazę filmów z bazą gatunków, tak aby w bazie filmów można było odczytać nazwę gatunku filmu.
df_merge = pd.merge(genres,movies_cleaned,how='inner',on='genre_id')
#print(df_merge)

#Zwróć listę 10 najwyżej ocenianych filmów (vote_average), których liczba głosów (vote_count) jest większa od 3. kwartyla rozkładu liczby głosów.
q3 = np.round(np.quantile(df_merge.loc[df_merge['popularity'].notnull(), 'popularity'].values, 0.75))
print(f'kwartyl {q3}')
df_10_thebest_movies = df_merge[df_merge['popularity'] > q3]
df_10_thebest_movies = df_10_thebest_movies.sort_values(['vote_average'], ascending=False).head(10)
#print(df_10_thebest_movies)
#Jaki gatunek filmu z bazy pojawia się w niej najczęściej? Ile filmów tego gatunku znajduje się w bazie?
df_genre = df_merge[['title','genres','genre_id']].groupby(['genres']).count().reset_index()
df_genre.rename(columns={'genre_id':'total_number_per_genres'}, inplace=True)
df_genre = df_genre.sort_values(['total_number_per_genres'], ascending=False).head(1)
#Drama 1207total_number_per_genres
#print(df_genre)
#Filmy, którego gatunku trwają średnio najdłużej (runtime)?
df_runtime = df_merge[['title','genres','runtime','genre_id']].groupby(['genres', 'runtime']).mean().reset_index()
df_runtime.rename(columns={'genre_id':'runtime_mean'}, inplace=True)
df_runtime = df_runtime.sort_values(['runtime_mean'], ascending=False).head(10)
#(df_runtime)
## czt aby napewno o to chodzilo
'''Pogrupuj tabelę w taki sposób, aby otrzymać średni przychód (revenue) 
oraz średni budżet (budget) w danym roku dla filmów opublikowanych od 2010 (włącznie) do 2016 roku (włącznie). 
Następnie na tej podstawie stwórz wykres, 
w którym średnie przychody są wykresem kolumnowym, 
a średni budżet wykresem liniowym na tych samych osiach.
Sformatuj odpowiednio oś X oraz oś Y. Dodaj tytuł wykresu, oraz legendę,
która znajduje się w prawym górnym rogu płótna, lecz poza obszarem osi. Przykład wykresu widoczny poniżej:'''
# filmy filmów opublikowanych od 2010 (włącznie) do 2016 roku (włącznie)
df_movies_2010_2016 = df_merge[df_merge['release_date'].between('2010-01-01','2016-12-31')]
df_movies_2010_2016['release_date'] = pd.to_datetime(df_movies_2010_2016['release_date'])
print(df_movies_2010_2016.release_date)


                                                                                       


# In[2]:


df_movies_2010_2016_v2 = df_movies_2010_2016[['release_date','budget','revenue']]
print(df_movies_2010_2016_v2.columns)


# In[3]:


df_movies_2010_2016_v2 = df_movies_2010_2016_v2.groupby(pd.Grouper(key='release_date',freq='Y')).mean().reset_index()
df_movies_2010_2016_v2


# movies.sample

# In[4]:


#df_movies_2010_2016_v2['budget'] = df_movies_2010_2016_v2['budget'].apply(lambda x: '{:.2f}'.format(x))
'''
df_movies_2010_2016_v2['budget'] = (df_movies_2010_2016_v2['budget']).astype(float)
df_movies_2010_2016_v2['budget'] = round((df_movies_2010_2016_v2['budget'])/1000000,2)
df_movies_2010_2016_v2['revenue'] = df_movies_2010_2016_v2['revenue'].astype(float)
df_movies_2010_2016_v2['revenue'] = round(df_movies_2010_2016_v2['revenue']/1000000,2)
print(df_movies_2010_2016_v2)
'''


# In[5]:


df_movies_2010_2016_v2['release_date'] = pd.DatetimeIndex(df_movies_2010_2016_v2['release_date']).year
print(df_movies_2010_2016_v2)


# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
fig = plt.figure(figsize=(12,6))
ax = fig.add_axes([0,0,1,1])

plt.title('Sredni przychod i dochod z filmow w latach 2010-2016', fontsize=15)
#df_movies_2010_2016_v2['revenue'].plot(kind='bar')
#sns.barplot(x=years, y ='revenue', data=df_movies_2010_2016)
#plotly
def million(x, pos):
        return '{:2.1f}M'.format(x*1e-6)

formatter = plt.FuncFormatter(million)

ax.yaxis.set_major_formatter(formatter)

x = list(df_movies_2010_2016_v2['release_date'][:7])
y = list(df_movies_2010_2016_v2['revenue'][:7])
y2 = list(df_movies_2010_2016_v2['budget'][:7])

plt.bar(x, y,label="revenue")
plt.plot(x,y2, color = 'red', label="budget")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#sns.lineplot(x='release_date', y ='budget', data=df_movies_2010_2016_v2)


# In[7]:


df_movies_2010_2016_v2['budget']


# Stwórz histogram czasu trwania filmów z gatunku, który cechuje się największym średnim czasem trwania.

# In[8]:


df_runtime  = df_runtime[ df_runtime['genres'] =='TV Movie']
df_runtime


# In[9]:


sns.histplot(df_runtime['runtime'])


# In[ ]:




