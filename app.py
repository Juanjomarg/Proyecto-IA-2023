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
            style={'padding-left':'20em','padding-right':'20em'}
        ),
        html.Footer(
            children=[
                dbc.Container(
                    [
                        html.P('''De Colombia pal mundo''',style={'padding-top':'2em'}),
                        html.P('''Desarrollado por: Juan José Martínez Guerrero'''),
                        html.P('''Todos los derechos reservados'''),
                    ]
                )
            ],
        ),
        html.Img(src='./static/color-scheme-left.svg',style={'position':'absolute','width':'500px','heigth':'500px','bottom':'0','left':'0'}),
        html.Img(src='./static/color-scheme-right.svg',style={'position':'absolute','width':'500px','heigth':'500px','bottom':'0','right':'0'}),
    ],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)