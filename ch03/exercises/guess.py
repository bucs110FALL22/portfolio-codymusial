import random

num = random.randint(1, 10)
num_guesses = 0

for i in range(3):
  guess_num = int(input("Guess a number between 1 and 10: "))
  num_guesses += 1
  if guess_num > num:
    print("Too High")
  elif guess_num < num:
    print("Too Low")
  else:
    print("Correct!")
    correct_guess = True

print("You took you", num_guesses, "tries")