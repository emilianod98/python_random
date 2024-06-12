# ASPECT RATIO DE UNA IMAGEN.
#
#------------------------------------------------------------------
#
# Crea un programa que se encargue de calcular el aspect ratio de una
# imagen a partir de una url.
# - Url de ejemplo:
#   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
# - Por ratio hacemos referencia por ejemplo a los "16:9" de una
#   imagen de 1920*1080px.
#
#------------------------------------------------------------------

import requests
from PIL import Image
from io import BytesIO

def get_image_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))

def calculate_aspect_ratio(image):
    width, height = image.size
    aspect_ratio = width / height
    return aspect_ratio

def main():
    url = input("Introduce la URL de la imagen: ")
    try:
        image = get_image_from_url(url)
        aspect_ratio = calculate_aspect_ratio(image)
        print(f"El aspecto de la imagen es: {aspect_ratio:.2f}")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

if __name__ == "__main__":
    main()
