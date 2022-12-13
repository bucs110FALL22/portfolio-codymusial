import requests
from Crypto import Crypto
from Exchange import Exchange

class Run:
  def __init__(self):
    self.api1 = Crypto()
    self.api2 = Exchange()
  def execute(self):
    go = True
    while go:
      self.api1.get_realtime_value()
      print("")
      self.api2.get_rate()
      print("")
run = Run()
run.execute()



# Get the real-time value of Bitcoin in USD
bitcoin_value = self.api1.get_realtime_value("BTC/USD")


# Get the exchange rate between EUR and USD
eur_usd_rate = self.api2.get_rate("EUR", "USD")

print(bitcoin_value, eur_usd_rate)

