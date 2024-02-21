import requests

API_KEY = 'fca_live_HC6ZAAfRvea2RDgBdVrj7p2lyW5KO0CWYaKYWPYz'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES = ["USD", "CAD", "EUR", "AUD"]

def convert_currency(base):
    currencies = ','.join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an exception if the request failed
        data = response.json()
        return data["data"]
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except KeyError:
        print(f"Unexpected response format: {response.text}")
while True:
    base = input("Enter the base currency (q for quit): ").upper()

    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")

