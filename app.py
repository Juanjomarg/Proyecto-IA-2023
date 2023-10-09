from assets.libraries import *
from assets.navbar import *

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.COSMO, dbc.icons.FONT_AWESOME,"https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap"],
    use_pages=True
)
server=app.server

app.layout = dbc.Container(
    children=
        [
            navbar,
            html.Div(
                [
                    dash.page_container
                ],
                className="content",
                style={'padding-left':'20em','padding-right':'20em'}
            ),
        ],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)