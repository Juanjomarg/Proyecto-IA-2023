from assets.libraries import *

def decode_img(contents):
    formatted_content= contents.replace('data:image/png;base64,','')

    decoded = base64.b64decode(formatted_content)

    pil_image = Image.open(io.BytesIO(decoded)).resize((160,160)).convert("RGB") 
    image = np.asarray(pil_image)
    batch = np.expand_dims(image, axis=0)
    return batch

class_labels = ['Invierno', 'Otoño', 'Primavera', 'Verano']

def predict_img(model,image):
    decoded=decode_img(image)

    inp=decoded.reshape((-1,160,160,3))
    prediction=model.predict(inp).flatten()
    index=prediction.argmax()
    print(class_labels[index])

    inv=html.P('Felicidades, tu estacionalidad es el invierno, los colores con un croma neutral son mas lo tuyo')
    inv_no=html.P('Por otro lado intenta evitar los colores tierra y pasteles porque te pueden opacar')

    ver=html.P('Felicidades, tu estacionalidad es verano, los colores que te favorecen aquellos que tienen un chroma bajo, opacos')
    ver_no=html.P('Por otro lado intenta evitar los colores con base amarilla, dorada y el negro')

    pri=html.P('Felicidades, tu estacionalidad es la primavera, los colores vivos y brillantes son lo tuyo')
    pri_no=html.P('Por otro lado intenta evitar colores tierra, pastel porque pueden opacar la luz de tu rostro')

    oto=html.P('fff')
    oto_no=html.P('fff')

    else_si=html.P('Wow, tienes tremendo estilo, pero no logramos reconocer tu estación')
    else_no=html.P('No reconocemos tu estación, pero por tu foto a tí todo te queda bien')

    ########################################################################
    # Invierno
    ########################################################################

    if class_labels[index]=='Invierno': # Listo
        si=inv
        no=inv_no
        f1={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#EF566A',
            }
        f2={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#EB1383',
            }
        f3={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#DD76BD',
            }
        f4={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#68CCFF',
            }
        f5={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#FEF365',
            }
        f6={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#F05654',
            }
        n1={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#F8B4C3',
            }
        n2={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#FAB19E',
            }
        n3={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#A39E38',
            }
        n4={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#767A93',
            }
        n5={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#965B6D',
            }
        n6={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#E2BD4B',
            }

    ########################################################################
    # Otono
    ########################################################################

    elif class_labels[index]=='Otoño':
        si=oto
        no=oto_no
        f1={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#EFABBA',
            }
        f2={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#574398',
            }
        f3={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#6CCACF',
            }
        f4={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#DDFFFF',
            }
        f5={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#B9AC35',
            }
        f6={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#671112',
            }
        n1={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#D4DF28',
            }
        n2={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#181947',
            }
        n3={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#F01C1E',
            }
        n4={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#F7EF21',
            }
        n5={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#F0592A',
            }
        n6={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#fff',
            }

    ########################################################################
    # Primavera
    ########################################################################

    elif class_labels[index]=='Primavera': # Listo
        si=pri
        no=pri_no
        f1={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#F14469',
            }
        f2={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#4754AD',
            }
        f3={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#15B9F1',
            }
        f4={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#33BD44',
            }
        f5={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#F3F20A',
            }
        f6={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#ED4727',
            }
        n1={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#9DB0B6',
            }
        n2={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#596577',
            }
        n3={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#BAA3AD',
            }
        n4={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#6F2A2D',
            }
        n5={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#7B4A1F',
            }
        n6={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#D4A45A',
            }

    ########################################################################
    # Verano
    ########################################################################

    elif class_labels[index]=='Verano':
        si=ver
        no=ver_no
        f1={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#9A2132',
            }
        f2={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#BB488B',
            }
        f3={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#7766AA',
            }
        f4={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#114143',
            }
        f5={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#CCEECD',
            }
        f6={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#82725E',
            }
        n1={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#8F3F1E',
            }
        n2={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#D9B428',
            }
        n3={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#9A1F27',
            }
        n4={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'##0A060E',
            }
        n5={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#EA8B1F',
            }
        n6={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#B73D26',
            }

    ########################################################################
    # Else
    ########################################################################

    else:
        si=else_si
        no=else_no
        f1={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#fff',
            }
        f2={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#fff',
            }
        f3={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#fff',
            }
        f4={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#fff',
            }
        f5={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#fff',
            }
        f6={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#fff',
            }
        n1={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#fff',
            }
        n2={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#fff',
            }
        n3={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#fff',
            }
        n4={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#fff',
            }
        n5={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#fff',
            }
        n6={
                'width':'60px',
                'height':'60px',
                'border-radius': '20%',  # Creates a circle
                'display': 'flex', # Flexbox
                'textAlign': 'center', # Centrar texto horizontal
                'justify-content': 'center', # Centrar elementos horizontalmente
                'align-items': 'center', # Centrar elementos verticalmente
                'margin':'10px',
                'background':'#fff',
            }

    ########################################################################
    # Imagen
    ########################################################################
    
    img=html.Img(
        src=image,
        style={
            'width': '100%',
            'height': '300px',
            'object-fit': 'cover',
            
            'display': 'flex', # Flexbox
            'textAlign': 'center', # Centrar texto horizontal
            'justify-content': 'center', # Centrar elementos horizontalmente
            'align-items': 'center', # Centrar elementos verticalmente
            'margin': 'auto',
        }
    )

    return img,f1,f2,f3,f4,f5,f6,n1,n2,n3,n4,n5,n6,si,no
    


