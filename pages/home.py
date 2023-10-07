from assets.libraries import *
from assets.drag_and_drop import *


dash.register_page(__name__, path='/')

layout = html.Div([
    drag_and_drop,
])