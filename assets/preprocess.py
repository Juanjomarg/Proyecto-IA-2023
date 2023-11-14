from assets.libraries import *

def preprocesar_img(contents):
    salida= html.Div(
        html.Img(
            src=contents,
            className='custom-image',
            style={
                'width': '100%',
                'height': '300px',
                'object-fit': 'cover',
                #'border-radius': '10%',
                
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin': 'auto',
            }
        ),
        className='custom-div'
    )
    return salida