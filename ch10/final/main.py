import requests

class CryptocurrencyAPI:
    def __init__(self):
        self.base_url = "https://www.worldcoinindex.com/apiservice/ticker?key={key}&label=ethbtc-ltcbtc&fiat=btc"
        self.key = "YjTqU5C0MelSxuklPtTJRLsL1zlWqwiszaG"

    def get_realtime_value(self, symbol):
        self.api_url = self.base_url + "?key=" + self.key + "&label=" + symbol + "&fiat=btc"
        response = requests.get(self.api_url)
        if response.status_code == 200:
            
            return response.json()
        else:
            return None

class ExchangeRateAPI:
    def __init__(self):
        self.base_url = "https://api.currencybeacon.com/v1/latest"
        self.key = "277c4a7dbf7fb18ebaa4d94a0e6a115c"

    def get_rate(self, from_currency, to_currency):
        url = self.base_url + "?key=" + self.key + "&q=" + from_currency + "-" + to_currency
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

# Create an instance of the CryptocurrencyAPI
crypto_api = CryptocurrencyAPI()

# Get the real-time value of Bitcoin in USD
bitcoin_value = crypto_api.get_realtime_value("BTC/USD")

# Create an instance of the ExchangeRateAPI
exchange_api = ExchangeRateAPI()

# Get the exchange rate between EUR and USD
eur_usd_rate = exchange_api.get_rate("EUR", "USD")

print(crypto_api, bitcoin_value, exchange_api, eur_usd_rate)