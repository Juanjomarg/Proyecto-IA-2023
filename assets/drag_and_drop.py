from assets.libraries import *

drag_and_drop = html.Div([
    dcc.Upload(
        id='subir_imagen',
        children=html.Div([
            html.A('Drag and Drop or Select Files')
        ]),
        style={
            'width': '100%',
            'height': '200px',

            'borderWidth': '1px', # Grosor de linea
            'borderStyle': 'dashed', # Estilo de linea
            'borderRadius': '5px', # Redondeo puntas cuadrado

            
            'display': 'flex', # Flexbox
            'textAlign': 'center', # Centrar texto horizontal
            'justify-content': 'center', # Centrar elementos horizontalmente
            'align-items': 'center', # Centrar elementos verticalmente
            'margin': 'auto',
        },
        multiple=False
    ),
])