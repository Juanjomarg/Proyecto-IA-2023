from assets.libraries import *


dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('Welcome to the Home Page'),
])