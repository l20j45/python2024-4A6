import requests
from bs4 import BeautifulSoup

def obtener_tipo_cambio():
    url = 'https://www.xe.com/es/currencyconverter/convert/?Amount=1&From=USD&To=MXN'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        # Encuentra el elemento que contiene el tipo de cambio
        tipo_cambio_elemento = soup.find('span', class_='converterresult-toAmount')
        tipo_cambio = tipo_cambio_elemento.text.strip()
        return tipo_cambio
    except AttributeError:
        return "No se pudo encontrar el tipo de cambio. La estructura de la página puede haber cambiado."

if __name__ == "__main__":
    tipo_cambio = obtener_tipo_cambio()
    print(f"El tipo de cambio actual es de 1 USD a {tipo_cambio} MXN")
