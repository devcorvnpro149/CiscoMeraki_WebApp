from dash import html
from dash import dcc
from dash.dependencies import Output, Input

from dash_extensions import Lottie       
import dash_bootstrap_components as dbc  


from app import app
# from app import server

from apps import build_pie, build_bar, build_scatter_geo, build_map_density
         

# Lottie by Emil - https://github.com/thedirtyfew/dash-extensions
url_build_pie = 'https://assets4.lottiefiles.com/packages/lf20_n6jcgmuo.json'
url_build_bar = 'https://assets4.lottiefiles.com/packages/lf20_noz9pzmw.json'
url_build_map_density = 'https://assets4.lottiefiles.com/packages/lf20_ftcfknxp.json'
url_build_scatter_geo = 'https://assets4.lottiefiles.com/packages/lf20_q4m6OS.json'
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))


# Bootstrap themes by Ann: https://hellodash.pythonanywhere.com/theme_explorer
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src='/assets/ciscomeraki.png') 
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Br(),
                    html.H1('Dashboard', style = {'textAlign':'center', 'color':'white'}, className = 'card-title'),
                ])
            ], color="dark", style={'height':'20vh'}),
        ], width=9),
    ],className='mb-2 mt-2'),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="32%", height="32%", url=url_build_pie)),
                dbc.CardBody([
                    dbc.CardLink(html.H5('Network Info'), href='/apps/build_pie')
                ], style={'textAlign':'center'})
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="32%", height="32%", url=url_build_bar)),
                dbc.CardBody([
                    dbc.CardLink(html.H5('Network ProductType'), href='/apps/build_bar')
                ], style={'textAlign':'center'})
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="32%", height="32%", url=url_build_map_density)),
                dbc.CardBody([
                    dbc.CardLink(html.H5('Network Density'), href='/apps/build_map_density')
                ], style={'textAlign': 'center'})
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="42%", height="42%", url=url_build_scatter_geo)),
                dbc.CardBody([
                    dbc.CardLink(html.H5('Where Your Network?'), href='/apps/build_scatter_geo')
                ], style={'textAlign': 'center'})
            ]),
        ], width=3),
    ],className='mb-2'),

    html.Br(),
    html.Br(),
    html.Br(),
    dcc.Location(id='url', refresh=False, pathname =''),
    html.Div(id='page-content', children=[])

], fluid=True)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
              
def display_page(pathname):
    if pathname == '/apps/build_pie':
        return build_pie.layout
    if pathname == '/apps/build_bar':
        return build_bar.layout
    if pathname == '/apps/build_scatter_geo':
        return build_scatter_geo.layout
    if pathname == '/apps/build_map_density':
        return build_map_density.layout
    else:
        return dbc.CardImg(src='/assets/picture1.png')


if __name__=='__main__':
    app.run_server(debug=True, port=8003)
