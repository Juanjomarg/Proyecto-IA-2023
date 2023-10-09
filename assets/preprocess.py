from assets.libraries import *

def preprocesar_img(contents):
    salida=html.Div(
        children=[
            html.H1('Preprocesada'),
            #!AQUI HAY QUE PREPROCESAR
            html.Img(src=contents)
        ]
    )
    return salida