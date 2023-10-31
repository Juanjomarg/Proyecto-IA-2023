from assets.libraries import *

def preprocesar_img(contents):
    salida=html.Div(
        children=[
            html.Img(
                src=contents,
                style={
                    'width': '100%',
                    'height': '200px',
                })
        ]
    )
    return salida