import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
  guess = int(input("Give a number between 1 and 100: "))

  attempts += 1
  if guess == secret_number:
    print(f"Congratulations! You found it in {attempts} attempts.")
    break
  elif guess < secret_number:
    print("Too low! Try again.")
  else:
    print("Too high! Try again.")
    (input)