from assets.libraries import *

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

navbar = dbc.Navbar(
    html.Div(
        #html.A(
            dbc.Row(
                children=[
                    dbc.Col(
                        html.Img(src=PLOTLY_LOGO,height="60px",style={'padding':'.5em'}),
                    ),
                    dbc.Col(
                        dbc.NavbarBrand("Navbar"),
                    ),
                    dbc.Col(
                        dbc.NavbarBrand('Hi'),
                    ),
                ],
                align="center",
                justify="end",
                className="g-0",
            ),
            
            #href="/",
            #style={"textDecoration": "none"},
        #),
    ),
)

navbar = dbc.Navbar(
    dbc.Container(
    [
        html.A(
            dbc.Row([
                dbc.Col(html.Img(src=PLOTLY_LOGO,height="60px",style={'padding':'.5em'}),),
                dbc.Col(dbc.NavbarBrand("Nombre Sitio", className="ms-2")),    
            ],
            align="center", className="g-0"),
        href="/", style={"textDecoration": "none"}),
        dbc.Row([
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse([
                dbc.Nav([
                    dbc.NavItem(dbc.NavLink("Home")),
                    dbc.NavItem(dbc.NavLink("Help")),
                    dbc.NavItem(dbc.NavLink("About"))
                ])
            ],
            id="navbar-collapse", is_open=False, navbar=True)
        ],
        align="center", className="g-0")
    ],
    fluid=True,style={'padding':'1em'}),
dark=True,
color="dark")