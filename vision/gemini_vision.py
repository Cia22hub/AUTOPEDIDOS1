import google.generativeai as genai

from PIL import Image


# =====================================
# CONFIGURAR GEMINI
# =====================================

genai.configure(

    api_key="AIzaSyA0wj2ChORZEb3M2b8l75tN3mSY7WFhQbg"

)


# =====================================
# MODELO
# =====================================

model = genai.GenerativeModel(

    "gemini-1.5-flash"

)


# =====================================
# ANALIZAR IMAGEN
# =====================================

def analyze_order_image(image_path):

    image = Image.open(image_path)

    prompt = """

    Analiza esta imagen de pedido escrita a mano.

    Extrae:

    - nombre del cliente
    - productos
    - cantidades
    - presentaciones
    - unidades

    Devuelve SOLO JSON válido.

    Ejemplo:

    {
      "cliente": "Juan Perez",
      "pedidos": [
        {
          "producto": "Aceite",
          "cantidad": 2,
          "presentacion": 900,
          "unidad": "und"
        }
      ]
    }

    """

    response = model.generate_content(

        [

            prompt,

            image

        ]

    )

    return response.text