import requests

class Exchange:
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