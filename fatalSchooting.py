'''Pobierz bazę danych dotyczącą śmiertelnych interwencji policji w USA, a następnie wczytaj ją do obiektu DataFrame.
Przekształć tabelę w taki sposób, aby wskazywała zestawienie jednocześnie liczby ofiar interwencji według rasy (‘race’) oraz tego, czy wykazywały one oznaki choroby psychicznej (‘signs_of_mental_illness’).
Za pomocą Map, Applymap lub Apply dodaj do tego zestawienia kolumnę wskazującą jaki odsetek ofiar interwencji wykazywało oznaki choroby psychicznej dla każdej z ras. 
Odpowiedz, która z nich charakteryzuje się największym odsetkiem znamion choroby psychicznej podczas interwencji.
Dodaj kolumnę oznaczającą dzień tygodnia, w którym doszło do interwencji. Zlicz interwencje według odpowiedniego dnia tygodnia. 
Następnie stwórz wykres kolumnowy, tak aby dni tygodnia były uszeregowane od poniedziałku do niedzieli.
Wczytaj do projektu dane dotyczące populacji w poszczególnych stanach USA oraz dane dotyczące skrótów poszczególnych stanów. 
Połącz te bazy danych w taki sposób, aby móc policzyć do ilu incydentów w bazie dotyczącej śmiertelnych interwencji doszło w przeliczeniu na 1000 mieszkańców każdego ze stanów.'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set(style='darkgrid')
url = 'https://github.com/AgaIrma/dataScienceBootcamp/blob/master/fatal-police-shootings-data.csv'

### Read csv
df = pd.read_csv('C:/Users/aga/Downloads/fatal-police-shootings-data.csv')
#print(df)
df.drop(['id','name'], axis=1, inplace=True)
print(df.isna().sum())
df.flee.value_counts()
df.flee.fillna('Not fleeing', inplace=True)
df.armed.value_counts()
df.armed.fillna(df.armed.value_counts().index[0], inplace=True)
df.dropna(axis=0, how='any', inplace=True)
#Przekształć tabelę w taki sposób, aby wskazywała zestawienie jednocześnie liczby ofiar interwencji według rasy (‘race’) oraz tego, czy wykazywały one oznaki choroby psychicznej (‘signs_of_mental_illness’).
print('jestem tutaj')
df_race = df[['race','signs_of_mental_illness','armed']].groupby(['race','signs_of_mental_illness']).count().reset_index()
df_race.rename(columns={'armed':'number_of_deaths'}, inplace=True)
#print(df_race)
def mental_illness_percentage(x,y):
    total_number_dead_per_race = df3[x]
    return y/total_number_dead_per_race
#Za pomocą Map, Applymap lub Apply dodaj do tego zestawienia kolumnę wskazującą jaki odsetek ofiar interwencji wykazywało oznaki choroby psychicznej dla każdej z ras. 
df3 = df[['race', 'armed']].groupby(['race']).count().reset_index()
df3.rename(columns={'armed':'number_of_dead_per_race'}, inplace=True)
map_race_total_deaths = dict(zip(df3['race'].unique(),df3['number_of_dead_per_race']))
df_race['number_of_dead_per_race'] = df_race['race'].map(map_race_total_deaths)
#print(df_race)
def percentage(row):
    return str(round((row['number_of_deaths'] / row['number_of_dead_per_race'])*100,2))

df_race['mental_illness_percentage_per_race'] = df_race.apply(lambda row: percentage(row),axis=1)
#Odpowiedz, która z nich charakteryzuje się największym odsetkiem znamion choroby psychicznej podczas interwencji.
df_4 = df_race[df_race['signs_of_mental_illness']==True]
df_4 = df_4.sort_values(by=['mental_illness_percentage_per_race'], ascending=False)
#print(df_4)
#Dodaj kolumnę oznaczającą dzień tygodnia, w którym doszło do interwencji. Zlicz interwencje według odpowiedniego dnia tygodnia. 
df['weekday']= pd.to_datetime(df['date']).dt.day_of_week
#print(df)
df_weekday = df[['race','weekday','armed']].groupby(['weekday']).count().reset_index()
df_weekday.rename(columns={'armed':'number_of_deaths_per_weekday'}, inplace=True)
days = {0:'Mon',1:'Tues',2:'Weds',3:'Thurs',4:'Fri',5:'Sat',6:'Sun'}

df_weekday['day_of_week'] = df_weekday['weekday'].apply(lambda x: days[x])
#print(df_weekday)
#Następnie stwórz wykres kolumnowy, tak aby dni tygodnia były uszeregowane od poniedziałku do niedzieli.

plt.figure(figsize=(12,6))
plt.title('Daily Fatal Shootings', fontsize=15)
sns.barplot(x=df_weekday.day_of_week, y='number_of_deaths_per_weekday', data=df_weekday)

#Wczytaj do projektu dane dotyczące populacji w poszczególnych stanach USA oraz dane dotyczące skrótów poszczególnych stanów. 
df_population = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population', header =0)[0]
#print(df_population.columns)
df_population_cl= df_population[['State','Population estimate, July 1, 2019[2]']]
# zeby nowy data frame zbudowac z kilku kolumn podwojne nawiasy

#print(df_population_cl)
df_states = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations', skiprows= [0,1,2,3,4,5,6,7,8,9])[0]
df_states = df_states[['Unnamed: 0','Unnamed: 3']]
df_states.columns = ['State','Abbrevation State']

df_merge = pd.merge(df_states,df_population_cl,how='inner',on='State')
df_merge.columns = ['Orginal state','state', 'Population']
print(df_merge)
df_orginal = pd.read_csv('C:/Users/aga/Downloads/fatal-police-shootings-data.csv')

print(df_orginal)
df_death_per_state = df_orginal[['state','armed']].groupby('state').count().reset_index()
df_death_per_state.rename(columns={'armed':'number_of_deaths'}, inplace=True)
print(df_death_per_state)

df_merge2 = pd.merge(df_death_per_state,df_merge,how='inner',on='state')
print(df_merge2)

def deathsPer1000(row):
    return str(round((row['number_of_deaths'] *1000/ row['Population']),2))

df_merge2['death_perState_per_1000'] = df_merge2.apply(lambda row: deathsPer1000(row),axis=1)
print(df_merge2)
#df_race['number_of_dead_per_race'] = 
#print(df_race.groupby(['race']).count().reset_index())
#print(df_race)

#df_race = df[['race','armed']].groupby(['race']).count().reset_index()
#df_race.rename(columns={'armed':'number_of_deaths'}, inplace=True)

#print(df_race)