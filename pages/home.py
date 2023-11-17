from assets.libraries import *
from assets.predict import *

model_path= os.path.join('.','model','final_model.h5')

model=tf.keras.models.load_model(model_path)
dash.register_page(__name__, path='/')

layout = dbc.Container(
    [
    html.Div(
        id='output_drag_drop',
        children=[
            dbc.Row(
                children=[
                    dbc.Col(
                        children=[
                                html.H2(
                                    'Descubre el tipo de colorimetría al que perteneces y vuélvete más fashionista 🥸',
                                    style={
                                        'text-align':'center',
                                        'padding-top':'5rem',
                                        'padding-bottom':'5rem',
                                        }
                                ),
                                html.H1('DANOS UNA IMÁGEN TUYA',style={'text-align':'center'}),
                                html.H3('Y genera tu paleta de colores recomendados',style={'text-align':'center','padding-bottom':'5rem'}),
                                dcc.Upload(
                                    id='subir_imagen',
                                    children=html.Div([
                                        html.H3("¡Suéltala aquí cual confeti digital!")
                                    ]),
                                    style={
                                        'height': '200px',

                                        'borderWidth': '2px', # Grosor de linea
                                        'borderStyle': 'dashed', # Estilo de linea
                                        'borderRadius': '5px', # Redondeo puntas cuadrado

                                        
                                        'display': 'flex', # Flexbox
                                        'textAlign': 'center', # Centrar texto horizontal
                                        'justify-content': 'center', # Centrar elementos horizontalmente
                                        'align-items': 'center', # Centrar elementos verticalmente
                                        'margin': 'auto',
                                        'color':'whitesmoke',
                                    },
                                    multiple=False
                                ),

                        ],
                        width={"size": 8, "offset": 2},
                    ),
                ],        
            ),
        ]
    ),
    
    html.Div(
        id='output_imagen',
        children=[
            dbc.Row(
                children=[
                    dbc.Col(
                        children=[
                            html.H1('Hola, lindura 😍',
                                    style={'padding-top':'5rem','padding-bottom':'1rem'}
                            ),
                            html.P(children=[],id='descriptivo_largo',style={'text-align':'justify'}),
                            html.H3('...por lo tanto:'),
                        ],
                        width=6
                    ),
                    dbc.Col(
                        children=[

                            html.Div(
                                id='output_image_upload',
                                style={'padding-top':'5rem'}
                            ),
                        ],
                        width=5
                    ),
                ],
                justify="between",
                style={
                    'padding-bottom':'5rem',
                }
            ),
            
            dbc.Row(
                [
                    dbc.Col(
                        [
                        dbc.Row(
                            dbc.Col(
                                [
                                    html.H2(
                                        'Colores que te favorecen',
                                        style={
                                                'padding-bottom':'1rem',
                                                'font-weight':'900',
                                            }
                                    ),
                                    html.P(id='texto_si'),
                                ]
                            )
                        ),
                    ],
                    width=5,
                    ),

                    dbc.Col(
                        [
                        dbc.Row(
                            dbc.Col(
                                [
                                    html.H2(
                                        'Colores a evitar',
                                        style={
                                                'padding-bottom':'1rem',
                                                'font-weight':'900',
                                            }
                                    ),
                                    html.P(id='texto_no'),
                                ]
                            )
                        ),
                        ],
                    width=5,
                    ),
                ],
                justify="between",
            ),

            dbc.Row(
                [
                    dbc.Col(
                        [
                        dbc.Row(
                            dbc.Col(
                                id='favorecen',
                                children=[
                                    html.Div(
                                        id='f1',
                                        children=[
                                        ],
                                    ),
                                    html.Div(
                                        id='f2',
                                        children=[
                                        ],
                                    ),
                                    html.Div(
                                        id='f3',
                                        children=[
                                        ],
                                    ),
                                    html.Div(
                                        id='f4',
                                        children=[
                                        ],
                                    ),
                                    html.Div(
                                        id='f5',
                                        children=[
                                        ],
                                    ),
                                    html.Div(
                                        id='f6',
                                        children=[
                                        ],
                                    ),
                                ],
                                style={
                                    'display': 'flex', # Flexbox
                                    'justify-content': 'center', # Centrar elementos horizontalmente
                                    'align-items': 'center', # Centrar elementos verticalmente
                                },
                            ),
                        style={'display': 'flex', 'justify-content': 'space-between'},
                        ),
                        ],
                        width=6,
                    ),
                    dbc.Col(
                        [
                        dbc.Row(
                            dbc.Col(
                                id='no_favorecen',
                                children=[
                                    html.Div(
                                        id='n1',
                                        children=[
                                        ],
                                    ),
                                    html.Div(
                                        id='n2',
                                        children=[
                                        ],
                                    ),
                                    html.Div(
                                        id='n3',
                                        children=[
                                        ],
                                    ),
                                    html.Div(
                                        id='n4',
                                        children=[
                                        ],
                                    ),
                                    html.Div(
                                        id='n5',
                                        children=[
                                        ],
                                    ),
                                    html.Div(
                                        id='n6',
                                        children=[
                                        ],
                                    ),
                                ],
                                style={
                                    'display': 'flex', # Flexbox
                                    'justify-content': 'center', # Centrar elementos horizontalmente
                                    'align-items': 'center', # Centrar elementos verticalmente
                                },
                            ),
                        style={'display': 'flex', 'justify-content': 'space-between'},
                        ),
                        ],
                    width=5,
                    ),
                ],
                justify="between",
            )
        ]
    ),
    
    ],
),


@dash.callback(
        Output('output_image_upload', 'children'),
        Output('output_drag_drop', 'style'),
        Output('output_imagen', 'style'),

        Output('n1', 'style'),
        Output('n2', 'style'),
        Output('n3', 'style'),
        Output('n4', 'style'),
        Output('n5', 'style'),
        Output('n6', 'style'),

        Output('f1', 'style'),
        Output('f2', 'style'),
        Output('f3', 'style'),
        Output('f4', 'style'),
        Output('f5', 'style'),
        Output('f6', 'style'),

        Output('descriptivo_largo', 'children'),
        Output('texto_si', 'children'),
        Output('texto_no', 'children'),
        
        Input('subir_imagen', 'contents')
)
def update_output(content):
    if content is None:
        children=[]
        common_dict = {
            'width': '60px',
            'height': '60px',
            'border-radius': '20%',
            'display': 'flex',
            'textAlign': 'center',
            'justify-content': 'center',
            'align-items': 'center',
            'margin': '10px',
            'background': '#fff',
        }

        f1 = f2 = f3 = f4 = f5 = f6 = n1 = n2 = n3 = n4 = n5 = n6 = common_dict
        long='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce volutpat ipsum ac sapien varius fermentum. Aenean tincidunt risus vitae erat ultrices, sit amet tempor felis tempor. In vitae ante tincidunt, tincidunt risus vel, vestibulum leo. Aenean lobortis at lorem sed elementum. Donec mollis mauris lacus, sed mollis augue ornare sit amet. Vestibulum vel rutrum quam. Phasellus a arcu rutrum, tincidunt purus vitae, condimentum purus. Aliquam mattis faucibus eros.'
        si='Texto generico Si'
        no='Texto generico No'
        
        return children, {'display': 'inline'}, {'display': 'none'},f1,f2,f3,f4,f5,f6,n1,n2,n3,n4,n5,n6,long,si,no
    else:
        img,f1,f2,f3,f4,f5,f6,n1,n2,n3,n4,n5,n6,long,si,no=predict_img(model,content)
        children=[
            img
        ]
        return children, {'display': 'none'}, {'display': 'inline'},f1,f2,f3,f4,f5,f6,n1,n2,n3,n4,n5,n6,long,si,no