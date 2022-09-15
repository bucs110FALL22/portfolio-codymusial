import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

while guess != number:
  if guess < number:
    print("Too Low")
    guess = int(input("\nGuess a number between 1 and 10: "))
  else:
    print("Too High")
    guess = int(input("\nGuess a number between 1 and 10: "))

print("Correct!")