import random 

guess = int(input("Guess a number between 1 and 100: "))
num = random.randint(1, 100)
count = 1
while guess != num:
    if guess > num:
        count += 1
        guess = int(input("That guess is too high, try a smaller number: "))
    elif guess < num:
        count += 1
        guess = int(input("That guess is too low, try a larger number: "))

print("You guessed correctly after " + str(count) + " tries")

