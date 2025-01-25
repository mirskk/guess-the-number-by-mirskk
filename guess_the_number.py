import random

computer_choice = random.randint(1, 100)

while True:
    try:
        player_choice = int(input("Enter your number: "))
    except ValueError:
        print("Staaawp. Give me a number :(")
        continue

    if player_choice < computer_choice:
        print("Too low!")
    elif player_choice > computer_choice:
        print("Too high!")

    if player_choice == computer_choice:
        print("Congratulations, you guessed!")
        break