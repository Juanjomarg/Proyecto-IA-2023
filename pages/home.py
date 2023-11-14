from assets.libraries import *
from assets.preprocess import *

lorem1='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce volutpat ipsum ac sapien varius fermentum. Aenean tincidunt risus vitae erat ultrices, sit amet tempor felis tempor. In vitae ante tincidunt, tincidunt risus vel, vestibulum leo. Aenean lobortis at lorem sed elementum. Donec mollis mauris lacus, sed mollis augue ornare sit amet. Vestibulum vel rutrum quam. Phasellus a arcu rutrum, tincidunt purus vitae, condimentum purus. Aliquam mattis faucibus eros.'
lorem2='In hac habitasse platea dictumst. Aliquam et vestibulum erat. Aenean sed nibh sed arcu tristique sagittis eu at ligula. Pellentesque gravida in augue nec euismod. Sed hendrerit diam a eros sodales bibendum. Integer cursus ipsum eget magna lacinia, vel gravida felis imperdiet. Integer tristique posuere neque, id tempus leo auctor at. Vestibulum ut diam sit amet lacus mollis rhoncus dictum nec sem. Suspendisse dignissim mi ut mi molestie, scelerisque sodales justo varius. Vestibulum et metus diam. Mauris mauris libero, feugiat sed lobortis ut, pulvinar sit amet sapien. In cursus ipsum erat, quis pharetra tortor suscipit nec.'

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
                            html.P(lorem1,style={'text-align':'justify'}),
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
                                    html.P(lorem1),
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
                                    html.P(lorem2),
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
                                [
                                    html.Div(
                                        [
                                            html.P(
                                                'fff',
                                                style={
                                                    'color':'black',
                                                    'padding-top':'15px',
                                                }
                                                )
                                        ],
                                        style={
                                            'background':'#fff',
                                            'width':'60px',
                                            'height':'60px',
                                            'border-radius': '20%',  # Creates a circle

                                            'display': 'flex', # Flexbox
                                            'textAlign': 'center', # Centrar texto horizontal
                                            'justify-content': 'center', # Centrar elementos horizontalmente
                                            'align-items': 'center', # Centrar elementos verticalmente
                                            'margin':'10px'
                                        }
                                    ),
                                    html.Div(
                                        [
                                            html.P(
                                                'fff',
                                                style={
                                                    'color':'black',
                                                    'padding-top':'15px',
                                                }
                                                )
                                        ],
                                        style={
                                            'background':'#fff',
                                            'width':'60px',
                                            'height':'60px',
                                            'border-radius': '20%',  # Creates a circle

                                            'display': 'flex', # Flexbox
                                            'textAlign': 'center', # Centrar texto horizontal
                                            'justify-content': 'center', # Centrar elementos horizontalmente
                                            'align-items': 'center', # Centrar elementos verticalmente
                                            'margin':'10px'
                                        }
                                    ),
                                    html.Div(
                                        [
                                            html.P(
                                                'fff',
                                                style={
                                                    'color':'black',
                                                    'padding-top':'15px',
                                                }
                                                )
                                        ],
                                        style={
                                            'background':'#fff',
                                            'width':'60px',
                                            'height':'60px',
                                            'border-radius': '20%',  # Creates a circle

                                            'display': 'flex', # Flexbox
                                            'textAlign': 'center', # Centrar texto horizontal
                                            'justify-content': 'center', # Centrar elementos horizontalmente
                                            'align-items': 'center', # Centrar elementos verticalmente
                                            'margin':'10px'
                                        }
                                    ),
                                    html.Div(
                                        [
                                            html.P(
                                                'fff',
                                                style={
                                                    'color':'black',
                                                    'padding-top':'15px',
                                                }
                                                )
                                        ],
                                        style={
                                            'background':'#fff',
                                            'width':'60px',
                                            'height':'60px',
                                            'border-radius': '20%',  # Creates a circle

                                            'display': 'flex', # Flexbox
                                            'textAlign': 'center', # Centrar texto horizontal
                                            'justify-content': 'center', # Centrar elementos horizontalmente
                                            'align-items': 'center', # Centrar elementos verticalmente
                                            'margin':'10px'
                                        }
                                    ),
                                    html.Div(
                                        [
                                            html.P(
                                                'fff',
                                                style={
                                                    'color':'black',
                                                    'padding-top':'15px',
                                                }
                                                )
                                        ],
                                        style={
                                            'background':'#fff',
                                            'width':'60px',
                                            'height':'60px',
                                            'border-radius': '20%',  # Creates a circle

                                            'display': 'flex', # Flexbox
                                            'textAlign': 'center', # Centrar texto horizontal
                                            'justify-content': 'center', # Centrar elementos horizontalmente
                                            'align-items': 'center', # Centrar elementos verticalmente
                                            'margin':'10px'
                                        }
                                    ),
                                    html.Div(
                                        [
                                            html.P(
                                                'fff',
                                                style={
                                                    'color':'black',
                                                    'padding-top':'15px',
                                                }
                                                )
                                        ],
                                        style={
                                            'background':'#fff',
                                            'width':'60px',
                                            'height':'60px',
                                            'border-radius': '20%',  # Creates a circle

                                            'display': 'flex', # Flexbox
                                            'textAlign': 'center', # Centrar texto horizontal
                                            'justify-content': 'center', # Centrar elementos horizontalmente
                                            'align-items': 'center', # Centrar elementos verticalmente
                                            'margin':'10px'
                                        }
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
                                [
                                    html.Div(
                                        [
                                            html.P(
                                                'fff',
                                                style={
                                                    'color':'black',
                                                    'padding-top':'15px',
                                                }
                                                )
                                        ],
                                        style={
                                            'background':'#fff',
                                            'width':'60px',
                                            'height':'60px',
                                            'border-radius': '20%',  # Creates a circle

                                            'display': 'flex', # Flexbox
                                            'textAlign': 'center', # Centrar texto horizontal
                                            'justify-content': 'center', # Centrar elementos horizontalmente
                                            'align-items': 'center', # Centrar elementos verticalmente
                                            'margin':'10px'
                                        }
                                    ),
                                    html.Div(
                                        [
                                            html.P(
                                                'fff',
                                                style={
                                                    'color':'black',
                                                    'padding-top':'15px',
                                                }
                                                )
                                        ],
                                        style={
                                            'background':'#fff',
                                            'width':'60px',
                                            'height':'60px',
                                            'border-radius': '20%',  # Creates a circle

                                            'display': 'flex', # Flexbox
                                            'textAlign': 'center', # Centrar texto horizontal
                                            'justify-content': 'center', # Centrar elementos horizontalmente
                                            'align-items': 'center', # Centrar elementos verticalmente
                                            'margin':'10px'
                                        }
                                    ),
                                    html.Div(
                                        [
                                            html.P(
                                                'fff',
                                                style={
                                                    'color':'black',
                                                    'padding-top':'15px',
                                                }
                                                )
                                        ],
                                        style={
                                            'background':'#fff',
                                            'width':'60px',
                                            'height':'60px',
                                            'border-radius': '20%',  # Creates a circle

                                            'display': 'flex', # Flexbox
                                            'textAlign': 'center', # Centrar texto horizontal
                                            'justify-content': 'center', # Centrar elementos horizontalmente
                                            'align-items': 'center', # Centrar elementos verticalmente
                                            'margin':'10px'
                                        }
                                    ),
                                    html.Div(
                                        [
                                            html.P(
                                                'fff',
                                                style={
                                                    'color':'black',
                                                    'padding-top':'15px',
                                                }
                                                )
                                        ],
                                        style={
                                            'background':'#fff',
                                            'width':'60px',
                                            'height':'60px',
                                            'border-radius': '20%',  # Creates a circle

                                            'display': 'flex', # Flexbox
                                            'textAlign': 'center', # Centrar texto horizontal
                                            'justify-content': 'center', # Centrar elementos horizontalmente
                                            'align-items': 'center', # Centrar elementos verticalmente
                                            'margin':'10px'
                                        }
                                    ),
                                    html.Div(
                                        [
                                            html.P(
                                                'fff',
                                                style={
                                                    'color':'black',
                                                    'padding-top':'15px',
                                                }
                                                )
                                        ],
                                        style={
                                            'background':'#fff',
                                            'width':'60px',
                                            'height':'60px',
                                            'border-radius': '20%',  # Creates a circle

                                            'display': 'flex', # Flexbox
                                            'textAlign': 'center', # Centrar texto horizontal
                                            'justify-content': 'center', # Centrar elementos horizontalmente
                                            'align-items': 'center', # Centrar elementos verticalmente
                                            'margin':'10px'
                                        }
                                    ),
                                    html.Div(
                                        [
                                            html.P(
                                                'fff',
                                                style={
                                                    'color':'black',
                                                    'padding-top':'15px',
                                                }
                                                )
                                        ],
                                        style={
                                            'background':'#fff',
                                            'width':'60px',
                                            'height':'60px',
                                            'border-radius': '20%',  # Creates a circle

                                            'display': 'flex', # Flexbox
                                            'textAlign': 'center', # Centrar texto horizontal
                                            'justify-content': 'center', # Centrar elementos horizontalmente
                                            'align-items': 'center', # Centrar elementos verticalmente
                                            'margin':'10px'
                                        }
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


@dash.callback(Output('output_image_upload', 'children'),
               Output('output_drag_drop', 'style'),
               Output('output_imagen', 'style'),

              Input('subir_imagen', 'contents'),
              State('subir_imagen', 'filename'),
              State('subir_imagen', 'last_modified'))
def update_output(content, filename, date_upload):
    if content is None:
        children=[
        ]
        return children, {'display': 'inline'}, {'display': 'none'}
        #return children, {'display': 'none'}, {'display': 'inline'}
    else:
        children=[
            preprocesar_img(content)
        ]
        return children, {'display': 'none'}, {'display': 'inline'}