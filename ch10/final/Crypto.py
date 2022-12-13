import requests

class Crypto:
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