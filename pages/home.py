from assets.libraries import *
from assets.drag_and_drop import *
from assets.preprocess import *


dash.register_page(__name__, path='/')

layout = html.Div(
    [
    html.H2('Descubre el tipo de colorimetría al que perteneces y vuélvete más fashionista 🥰',style={'text-align':'center','padding-top':'5rem','padding-bottom':'3rem','width':'45rem','margin-inline':'auto'}),
    html.H1('DANOS UNA IMÁGEN TUYA',style={'text-align':'center'}),
    html.H3('Y genera tu paleta de colores recomendados',style={'text-align':'center','padding-bottom':'3rem'}),
    dbc.Row(
        [
            dbc.Col(
                id='col_drag_drop',
                children=[
                    drag_and_drop,
                ],
                style={'width': '100%'},
            ),
            dbc.Col(
                id='col_img_drag_drop',
                children=[
                    html.Div(
                        id='output_image_upload',
                    ),
                ],
                style={'width': '0%'},
            ),
        ],
        style={'padding':'2rem'}
    ),


    ]
),


@dash.callback(Output('output_image_upload', 'children'),
               Output('col_drag_drop', 'style'),
               Output('col_img_drag_drop', 'style'),

              Input('subir_imagen', 'contents'),
              State('subir_imagen', 'filename'),
              State('subir_imagen', 'last_modified'))
def update_output(content, filename, date_upload):
    if content is None:
        children=[
        ]
        return children, {'width': '100%'}, {'width': '0%','display': 'none'}
    else:
        children=[
            preprocesar_img(content)
        ]
        return children, {'width': '50%'}, {'width': '50%','display': 'inline'}