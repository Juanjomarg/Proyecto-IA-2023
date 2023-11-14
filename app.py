from assets.libraries import *
from assets.navbar import *

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.COSMO, dbc.icons.FONT_AWESOME,"https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap"],
    use_pages=True
)
server=app.server

app.layout = dbc.Container(
    [
        navbar,
        html.Div(
            dash.page_container,
            className="content",
        ),
        html.Footer(
            children=[
                dbc.Container(
                    [
                    ]
                )
            ],
            style={'position':'absolute','width':'100%','heigth':'500px','bottom':'0','left':'0'},
        ),
        html.Img(src='./static/images/color-scheme-left.svg',style={'position':'absolute','width':'500px','heigth':'500px','bottom':'0','left':'0'}),
        html.Img(src='./static/images/color-scheme-right.svg',style={'position':'absolute','width':'500px','heigth':'500px','bottom':'0','right':'0'}),
    ],
    fluid=True,
    style={'height': '100vh'},
)

if __name__ == "__main__":
    app.run_server(debug=True)