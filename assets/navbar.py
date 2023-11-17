from assets.libraries import *

PLOTLY_LOGO = "./static/images/logo.svg"



navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="60px")),
                        dbc.Col(dbc.NavbarBrand("Color Fashionista", className="ms-2", style={'color':'whitesmoke'})),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
        ]
    ),
    color="transparent",
    style={"height": "8em"}
)