import requests
 
# Define the URL for the API
url = "https://open.er-api.com/v6/latest/USD"
 
try:
    # Send a GET request to the API
    response = requests.get(url,verify=False)
    response.raise_for_status()  # Check for HTTP errors
 
    # Parse the JSON response
    data = response.json()
 

    # Get the exchange rate for Mexican Peso
    mxn_rate = data['rates']['MXN']
 
    print(f"El valor actual del dólar en pesos mexicanos es: {mxn_rate} MXN")
 
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")