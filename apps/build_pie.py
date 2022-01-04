# import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from app import app
import pandas as pd 
import pathlib
import plotly.express as px           

# df = pd.read_csv("data_build_dropdown.csv") 
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("data_build_pie.csv"))

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets) 
layout = html.Div([

    html.H2('Information about your network with Pie Graph', style={'textAlign' : 'center', 'font-weight' : 'bold'}),

    html.Div([
        html.Div([
            dcc.Graph(id='pie_graph1')
        ], className = 'six columns'),
        html.Div([
            dcc.Graph(id='pie_graph2')
        ], className = 'six columns')       
    ], className = 'row'),

    html.Div([
        html.Div([
            html.Label(['Choose information to show:'],style={'font-weight': 'bold'}),

            dcc.Dropdown(id='my_dropdown1',
                options=[
                    {'label': 'OG_id', 'value': 'OG_id'},
                    {'label': 'Area', 'value': 'Area'}
                ],
                optionHeight=35,                    #height/space between dropdown options
                value='OG_id'                       #dropdown value selected automatically when page loads
            )
        ], className = 'six columns'),
        
        html.Div([
            html.Label(['Choose information to show:'],style={'font-weight': 'bold'}),

            dcc.Dropdown(id='my_dropdown2',
                options=[
                    {'label': 'Health', 'value': 'Health'},
                    {'label': 'State', 'value': 'State'},
                    {'label': 'Num Devices', 'value': 'Num Devices'}
                ],
                optionHeight=35,                    #height/space between dropdown options
                value='Health'                      #dropdown value selected automatically when page loads
            )
        ], className = 'six columns')
    ], className = 'row')
])

#---------------------------------------------------------------
# Connecting the Dropdown values to the graph
@app.callback(
    Output(component_id='pie_graph1', component_property='figure'),
    Input(component_id='my_dropdown1', component_property='value'),
)

def update_pie1(value1):
    fig1 = px.pie(df,names=value1)
    fig1.update_traces(textinfo='percent+label')
    fig1.update_layout(title={'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig1

@app.callback(
    Output(component_id='pie_graph2', component_property='figure'),
    Input(component_id='my_dropdown2', component_property='value'),
)
    
def update_pie2(value2):
    fig2 = px.pie(df,names=value2)
    fig2.update_traces(textinfo='percent+label')
    fig2.update_layout(title={'font':{'size':28},'x':0.5,'xanchor':'center'})
    return fig2


# if __name__ == '__main__':
#     app.run_server(debug=True)