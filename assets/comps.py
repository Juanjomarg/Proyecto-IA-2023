from libraries import *

navbar = dbc.Navbar(
    dbc.Container(
        html.Div([
            dbc.Row([
                dbc.Col(
                    html.A([
                        dbc.NavbarBrand("Gestor de respuestas IIP 2023")
                    ],
                    href="/",
                    style={"textDecoration": "none"},
                    
                ),
                    width=7
                ),
                dbc.Col(
                    width=5
                )
            ]),
                      
        ],
        style={'display':'inline-block','position':'relative','width':'100%'},
        className='navbar'
        )   
    ),color="#f8f9fa"
)

sidebar = html.Div(
    [
        html.A([
                    ],
                    href="/",
                    style={"textDecoration": "none"},
                    
                ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className="fas fa-home me-2"), 
                        html.Span("Estadisticas")],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-chart-bar me-2"),
                        html.Span("Respuestas"),
                    ],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-bomb me-2"),
                        html.Span("Eventualmente..."),
                    ],
                    href="/",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)