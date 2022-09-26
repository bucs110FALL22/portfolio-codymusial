print(10*5)
print(10**2)
print(15/10)
print(15//10)
print(-15//10)
print(15%10)
print(10%15)
print(10%10)
print(0%10)
print(10/15)
# Better to write as 2/3

#Money exchange
rate = float(input("What is the exchange rate from Euros to US Dollars? "))
amount = float(input("How Many Euros would you like to exchange? "))
total = rate*amount
result = round(total - 3, 2)
print("You received $" + str(result))