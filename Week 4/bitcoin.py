import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    price_per_bitcoin = data["bpi"]["USD"]["rate_float"]
except (requests.RequestException, KeyError, ValueError):
    sys.exit("Error fetching data")

total_cost = bitcoins * price_per_bitcoin
print(f"${total_cost:,.4f}")
