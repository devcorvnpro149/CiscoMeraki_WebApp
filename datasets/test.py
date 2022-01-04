

# from app import app
import plotly.express as px


import pandas as pd

df = pd.read_csv("data_build_bar.csv")  

# filt = (df['OG_id'] == 681155)
# print (df[filt])
# dff = df[filt]
# print (df['OG_id'][0])
# fig = px.bar(data_frame = dff, x = dff['ProductType'], y = dff['Number of NWs supported'], color = dff['ProductType'])
# fig.show()

# fig = px.bar(data_frame = df, x = df['ProductType'], y = df['Number of supported NWs'])
# fig.update_traces(insidetextfont = dict(color = 'red', size = 5), outsidetextfont = dict(color = 'purple', size = 10))
# fig.show()

