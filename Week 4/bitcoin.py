import sys
import requests
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
API_KEY = "f6498fa5479106813be59c20fdb50373845993a9d33d648c578f2662262a7300"
try:
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    price_usd = float(data["data"]["priceUsd"])
    total_cost = bitcoins * price_usd
    print(f"${total_cost:,.4f}")
except requests.RequestException:
    sys.exit("Request failed")
