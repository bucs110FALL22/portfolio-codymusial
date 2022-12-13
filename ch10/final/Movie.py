import urllib3

http = urllib3.PoolManager()

class MovieAPI:
   def __init__(self):
       self.base_url = "https://movie-database-api.com"

   def get_movie_box_office(self, movie_id):
       # Make a request to the movie database API to get the box office earnings for the given movie
       response = requests.get(f"{self.base_url}/movies/{movie_id}/box_office")

       # Parse the response and return the box office earnings
       return response.json()["box_office"]

class CurrencyExchangeAPI:
   def __init__(self):
       self.base_url = "https://currency-exchange-api.com"

   def convert_currency(self, amount, from_currency, to_currency):
       # Make a request to the currency exchange API to convert the given amount from the given currency to the specified currency
       response = requests.get(f"{self.base_url}/convert?amount={amount}&from={from_currency}&to={to_currency}")

       # Parse the response and return the converted amount
       return response.json()["converted_amount"]

# Create an instance of the MovieAPI class
movie_api = MovieAPI()

# Get the box office earnings for a movie with the given ID
box_office = movie_api.get_movie_box_office(1234)

# Create an instance of the CurrencyExchangeAPI class
exchange_api = CurrencyExchangeAPI()

# Convert the box office earnings to a different currency
converted_box_office = exchange_api.convert_currency(box_office, "USD", "EUR")

response = requests.get(f"{self.base_url}/movies/{movie_id}/box_office")

now, replace that line with
response = http.request('GET', f"{self.base_url}/movies/"+movie_id+"/box_office")