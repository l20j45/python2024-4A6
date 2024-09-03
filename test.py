import requests

# Define the URL for the API
url = "https://api.exchangerate-api.com/v4/latest/USD"

try:
    # Send a GET request to the API
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors

    # Parse the JSON response
    data = response.json()

    print(data)
    # Get the exchange rate for Mexican Peso
    mxn_rate = data['rates']['MXN']

    print(f"El valor actual del dólar en pesos mexicanos es: {mxn_rate} MXN")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")
