import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer
import pandas as pd
import os
import pandas as pd
import seaborn as sns
sns.set()
import numpy as np
import matplotlib.pyplot as plt

cash_outlet = pd.read_csv('training.csv')

app = dash.Dash()

app.layout = html.Div([
                    
                    dcc.Graph(id='scatterplot', 
                        figure = px.scatter(df, x="bmi", y="charges", 
                            color="charges", title='cheapest fee and BMI')),
    
                    dcc.Graph(id='piechart', 
                        figure = px.pie(df, values='charges', names='region', 
                            color_discrete_sequence=px.colors.sequential.RdBu, 
                            title='Cheapest insurance fee by region')),

                    dcc.Graph(id='bargraph', 
                        figure = px.bar(df, x=df['age'], y=df['charges'],
                            hover_data=['age', 'charges'],
                            height=650, title='cheapest insurance fee by age')),

                    dcc.Graph(id='stacked bargraph',
                        figure = px.bar(df, x="sex", y="charges", 
                            height=650, 
                            title='gender that pays the least fee')),    

                    dcc.Graph(id='grouped bargraph', 
                        figure = px.bar(df, x="sex", y="charges", color='smoker', 
                            barmode ='group', height=650, 
                            title='gender that pays the least fee')),   

                    dcc.Interval(id='interval-component', 
                        interval=2000,
                        n_intervals=0)




                    ])



            
                            

if __name__ == '__main__':
    app.run_server(8058)