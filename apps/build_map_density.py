# import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from app import app
import pandas as pd 
import pathlib
import plotly.express as px  

# df = pd.read_csv("data_build_map_density.csv")  
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("data_build_map_density.csv"))

# app = dash.Dash(__name__)
layout = html.Div([

    html.H2('Information about your network with Map Density', style={'textAlign' : 'center', 'font-weight' : 'bold'}),

    html.Div([
        html.Label(['Choose your OG you want to show all NW locations:'], style={'font-weight': 'bold'}),
        dcc.RadioItems(id = 'my_radioitems',
            options = [
                {'label': x, 'value': x} for x in df['organizationId'].unique()
            ],
            value = df['organizationId'][0]
        )
    ]),
    html.Div(
       dcc.Graph(id = 'map_density')
    )
])

@app.callback(
    Output(component_id='map_density', component_property='figure'),
    Input(component_id='my_radioitems', component_property='value')
)

def update_map_density(OG_id):
    filt = (df['organizationId'] == OG_id)
    dff = df[filt] 
    fig = px.density_mapbox(dff, lat = 'latitude', lon = 'longitude', 
                            z='num_devices', radius = 10,
                            center = dict(lat = 9, lon = 9),
                            zoom = 1,
                            hover_name='name',
                            hover_data=['timeZone', 'productTypes'],
                            mapbox_style= 'open-street-map',
                            )
    return fig

# if __name__ == '__main__':
#     app.run_server(debug=True)

