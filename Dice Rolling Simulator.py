from random import randint # To generator random number


def Main():
    clear_screen = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

    while True:
        print("Welcome to guess the number: ")

        #  Creating the variables for the dice faces
        min_val = 1
        max_val = number_of_faces()

        # Calling the function to generate a random face
        random_num = random_face(min_val, max_val)

        # Starting the game
        play_game(random_num, max_val)

        # Asking the user if they want to replay
        replay = replay_the_game()
        if replay:
            print(clear_screen)
        elif not replay:
            print("\nOkay, goodbye. Thank you for playing.")
            break
        else:
            print("Error. Y or N not specified.")
            exit(1)


def replay_the_game():
    while True:
        replay = input("Do you want to replay the game [y/n] -> ")[0].lower()
        if replay == "y":
            return True
        elif replay == "n":
            return False
        else:
            print("Enter [Y]es or [N]o")


def number_of_faces():
    # Asking the user for the amount of faces
    while True:
        max_val = int(input("Enter the amount of faces the die has (Must be greater than 5 and divisible by 2): "))

        if max_val >= 6 and max_val % 2 == 0 and type(max_val) == int:
            break
        else:
            print("You were suppose to enter a number greater than 5 and divisible by 2!")
    return max_val


def random_face(min_val, max_val):
    print("Random number between {0} and {1} generated...\n".format(min_val, max_val))
    return randint(min_val, max_val)


def play_game(random_num, max_val):
    #  The below, if uncommented, will print the random number, was used to debug
    #  print("This is for testing purposes: {0}".format(random_num))

    tries = 3
    chance = 3  # Chances I give in case they guessed higher than the higher number

    while tries > 0:
        print("Tries left: {0}".format(tries))
        guess = abs(int(input("Enter a guess: ")))  # Absolute in case they put a negative

        if guess == random_num:
            print("Correct! The number was: {0}".format(random_num))
            break
        elif guess > max_val:  # If the guess was higher than the maximum value (The user chose it)
            if chance == 3:
                print("Calm down there.. The highest number is possible is {0} (2 Chances left)".format(max_val))
            elif chance == 2:
                print("I warned you already to not go above {0}. This is your last chance".format(max_val))
            elif chance == 1:
                print("You are trying to piss me off now?\n GAME OVER")
                break
            chance -= 1
        else:
            if guess > random_num:
                print("The number is lower...")
            if guess < random_num:
                print("The number is higher")

            tries -= 1

    print("Game over... You can out of tries.")

if __name__ == "__main__":
    Main()