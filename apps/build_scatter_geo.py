# import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from app import app
import pandas as pd 
import pathlib
import plotly.express as px  

# df = pd.read_csv("data_build_scatter_geo.csv")  
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("data_build_scatter_geo.csv"))

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
layout = html.Div([

    html.H2('Information about your network with Scatter Geo', style={'textAlign': 'center', 'font-weight': 'bold'}),

    html.Div([
        html.Div([
            html.Label(['Choose NW you want to show location:'], style={'font-weight': 'bold'}),
            dcc.RadioItems(id = 'my_radioitems',
                options = [
                    {'label': x, 'value': x} for x in df['name'].unique()
                ],
            value = df['name'][0]
            )
        ], className = 'six columns'),

        html.Div([
            dcc.Graph(id = 'scatter_geo')
        ], className = 'six columns')
    ], className = 'row')
])

@app.callback(
    Output(component_id='scatter_geo', component_property='figure'),
    Input(component_id='my_radioitems', component_property='value')
)

def update_scatter_geo(name):
    filt = (df['name'] == name)
    dff = df[filt] 
    fig = px.scatter_geo(dff,
                        locations = 'location',
                        projection= 'orthographic',
                        color = 'name',
                        opacity= .8,
                        hover_name = 'id',
                        hover_data = ['name','timeZone','productTypes']
                        )
    return fig

# if __name__ == '__main__':
#     app.run_server(debug=True)






   
