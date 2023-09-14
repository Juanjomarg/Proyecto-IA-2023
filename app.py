from assets.libraries import *
from assets.comps import *

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.COSMO, dbc.icons.FONT_AWESOME],
    use_pages=True
)
server=app.server

app.layout = dbc.Container(
    [
        navbar,
        sidebar,
        html.Div(
            [
                dash.page_container
            ],
            className="content",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)