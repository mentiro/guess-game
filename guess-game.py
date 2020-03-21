import random
tries = 1

print("*********************")
print("Welcome to RandGuess!")
print("*********************")
print("-- Try to guess the Secret Number! --")
print("")

name = input("What be your name? > ")
name = name.capitalize()

while True:
    try:
        age = int(input("What be your age, " + name + "? > "))
        print("You will have only " + str(len(name)) + " tries. Use them wisely!")
    except ValueError:
        print("This is not your age " + name + "! Try again... ")
        continue
    else:
        break

number = random.randint(0, age)
while tries <= len(name):
    while True:
        try:
            guess = int(input(">> Guess the secret number between 1 and " + str(age) + " > "))
        except ValueError:
            print("This is not a number " + name + "! Try again> ")
            continue
        else:
            break
    if guess > number:
        if tries >= len(name):
            print(" ")
            print("!--  No more tries...you lose - The Number was " + str(number) + "  --!")
            break
        print("Try lower. You are left with " + str((len(name)-tries)) + " tries.")
    elif guess < number:
        if tries >= len(name):
            print(" ")
            print("!--  No more tries...you lose - The Number was " + str(number) + "  --!")
            break
        print("Try higher. You are left with " + str((len(name)-tries)) + " tries.")
    else:
        print("------------------------------")
        print("Spot on " + name + "! " + str(number) + " is the right Guess")
        print("------------------------------")
        break
    tries += 1
