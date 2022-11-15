#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install dash


# In[2]:


import pandas as pd
import datetime as dt
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
class db:
    def __init__(self):
        self.transactions = db.transation_init()
        self.cc = pd.read_csv(r'db\country_codes.csv',index_col=0)
        self.customers = pd.read_csv(r'db\customers.csv',index_col=0)
        self.prod_info = pd.read_csv(r'db\prod_cat_info.csv')
        
@staticmethod
def transation_init():
    transactions = pd.DataFrame()
    src = r'db\transactions'
    for filename in os.listdir(src):
        transactions = transactions.append(pd.read_csv(os.path.join(src,filename),index_col=0))

    def convert_dates(x):
        try:
            return dt.datetime.strptime(x,'%d-%m-%Y')
        except:
            return dt.datetime.strptime(x,'%d/%m/%Y')

    transactions['tran_date'] = transactions['tran_date'].apply(lambda x: convert_dates(x))

    return transactions
def merge(self):
    df = self.transactions.join(self.prod_info.drop_duplicates(subset=['prod_cat_code'])
    .set_index('prod_cat_code')['prod_cat'],on='prod_cat_code',how='left')

    df = df.join(self.prod_info.drop_duplicates(subset=['prod_sub_cat_code'])
    .set_index('prod_sub_cat_code')['prod_subcat'],on='prod_subcat_code',how='left')

    df = df.join(self.customers.join(self.cc,on='country_code')
    .set_index('customer_Id'),on='cust_id')

    self.merged = df
    
df = db()
df.merge()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([],
                    style={'height':'100%'})

app.layout = html.Div([html.Div([],style={'width':'80%','margin':'auto'})],
                    style={'height':'100%'})

[dcc.Tabs(id='tabs',value='tab-1',children=[
                            dcc.Tab(label='Sprzedaż globalna',value='tab-1'),
                            dcc.Tab(label='Produkty',value='tab-2')
                            ]),
                            html.Div(id='tabs-content')]

app.layout = html.Div([html.Div([dcc.Tabs(id='tabs',value='tab-1',children=[
                            dcc.Tab(label='Sprzedaż globalna',value='tab-1'),
                            dcc.Tab(label='Produkty',value='tab-2')
                            ]),
                            html.Div(id='tabs-content')
                    ],style={'width':'80%','margin':'auto'})],
                    style={'height':'100%'})

if __name__ == '__main__':
    app.run_server(debug=True)
    

html.H1('Store_type',style={'text-align':'center'})

[dcc.DatePickerRange(id='sales-range',
                        start_date=df['tran_date'].min(),
                        end_date=df['tran_date'].max(),
                        display_format='YYYY-MM-DD')]

html.Div([dcc.DatePickerRange(id='sales-range',
                        start_date=df['tran_date'].min(),
                        end_date=df['tran_date'].max(),
                        display_format='YYYY-MM-DD')],style={'width':'100%','text-align':'center'})

html.Div([html.Div([dcc.Graph(id='bar-sales')],style={'width':'50%'}),
                        html.Div([dcc.Graph(id='choropleth-sales')],style={'width':'50%'})],style={'display':'flex'})



# In[ ]:




