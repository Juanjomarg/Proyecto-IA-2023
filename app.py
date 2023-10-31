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
            [
                dash.page_container
            ],
            className="content",
            style={'padding-left':'20em','padding-right':'20em'}
        ),
        
        html.Footer(
            #height='10em',
            #fixed=True,
            children=[
                dbc.Container(
                    [
                        html.P('De Colombia pal mundo',style={'padding-top':'2em'}),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.P('Desarrollado por: Juan José Martínez Guerrero'),
                                    ]
                                ),

                                dbc.Col(
                                    [

                                    ]
                                ),
                            ]
                        ),
                        html.P('Todos los derechos reservados'),
                    ]
                )
            ],
            style={
                    'color':'whitesmoke',
                    'background':'linear-gradient(90deg, rgba(92,69,143,1) 0%, rgba(31,132,178,1) 46%, rgba(33,196,140,1) 100%)',
                    'background-size': 'cover',
                    'background-repeat': 'no-repeat',
                }
        )
    ],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)