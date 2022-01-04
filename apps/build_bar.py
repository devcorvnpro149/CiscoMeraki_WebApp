# import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from app import app
import plotly.express as px
import pathlib
import pandas as pd

# df = pd.read_csv("data_build_bar.csv")  
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("data_build_bar.csv"))

# app = dash.Dash(__name__)
layout = html.Div([

    html.H2('Information about your network with Bar Chart', style={'textAlign' : 'center', 'font_weight' : 'bold'}),

    html.Div(
        dcc.Graph(id='bar_chart')
    ),

    html.Div([
        html.Label(['Choose OG to show:'],style={'font-weight': 'bold'}),
        dcc.Dropdown(id='my_dropdown',
            options=[
                {'label': x, 'value': x} for x in df['OG_id'].unique()
            ],
            value = df['OG_id'][0]
        )
    ])
])

@app.callback(
    Output(component_id='bar_chart', component_property='figure'),
    Input(component_id='my_dropdown', component_property='value')
)

def update_bar(OG_id):
    filt = (df['OG_id'] == OG_id)
    dff = df[filt]
    fig = px.bar(data_frame = dff, x = dff['ProductType'], y = dff['Number of supported NWs'], color = dff['Number of supported NWs'])
    # fig.update_layout(showlegend = False)
    return fig

# if __name__ == '__main__':
#     app.run_server(debug=True)






