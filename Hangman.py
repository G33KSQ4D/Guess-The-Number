import os # To check if file exists
from random import randint # To pick a random index in the word_list
import time # For sleep function


def main():
    print("\nWelcome to hangman v0.1")
    print("The hangman ASCII was created by me.")
    print("I hope you enjoy playing as much as I enjoyed making it!\n")

    # Getting all the words for the game
    word_list = read_word_list()

    while True:
        # Getting the random word
        word = generate_random_word(word_list)

        # The function for the actual game
        play_game(word)

        # Checking to see if the user wants to play again
        replay = game_over_replay()
        if replay:  # == True
            continue
            clear_window()
        elif not replay:  # replay == False
            print("Thank you for playing hangman.")
            break


def draw_hangman(index):
    hangman_list = [

        # Hangman 0
        [
            [' ', '|', '-', '-', '-', ' '],
            [' ', ' ', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', '/', '|', '\\'],
        ],

        # Hangman 1
        [
            [' ', '|', '-', '-', '-', ' '],
            [' ', 'O', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', '/', '|', '\\'],
        ],

        # Hangman 2
        [
            [' ', '|', '-', '-', '-', ' '],
            [' ', 'O', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', '/', '|', '\\'],
        ],

        # Hangman 3
        [
            [' ', '|', '-', '-', '-', ' '],
            [' ', 'O', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', '|', ' '],
            ['/', ' ', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', '/', '|', '\\'],
        ],

        # Hangman 4
        [
            [' ', '|', '-', '-', '-', ' '],
            [' ', 'O', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', '|', ' '],
            ['/', ' ', '\\', ' ', '|', ' '],
            [' ', ' ', ' ', '/', '|', '\\'],
        ],

        # Hangman 5
        [
            [' ', '|', '-', '-', '-', ' '],
            [' ', 'O', ' ', ' ', '|', ' '],
            ['\\', '|', ' ', ' ', '|', ' '],
            [' ', '|', ' ', ' ', '|', ' '],
            ['/', ' ', '\\', ' ', '|', ' '],
            [' ', ' ', ' ', '/', '|', '\\'],
        ],

        # Hangman 6
        [
            [' ', '|', '-', '-', '-', ' '],
            [' ', 'O', ' ', ' ', '|', ' '],
            ['\\', '|', '/', ' ', '|', ' '],
            [' ', '|', ' ', ' ', '|', ' '],
            ['/', ' ', '\\', ' ', '|', ' '],
            [' ', ' ', ' ', '/', '|', '\\'],
        ]
    ]

    for row in hangman_list[index]:
        print(" ".join(row))


def read_word_list():
    word_list = [] # Will contain all the words from the file
    file = input("Enter the word text file (Path or Name): ")

    while not os.path.isfile(file):  # Repeat until user enters valid file
        print("The file {0} doesn't exist.\n".format(file))
        file = input("Enter the word text file (Path or Name): ")  # or "WordList.txt"

    with open(file, "r") as list_file:
        for word in list_file: # Read every line
            #  print(word.strip("\n")) # Strips the new line
            word_list.append(word.strip("\n"))
    return word_list


def generate_random_word(word_list):
    return "".join(word_list[randint(0, len(word_list)-1)])


def check_if_win(current_word):
    did_win = True
    for letter in current_word:
        if letter == "_":
            did_win = False
    return did_win


def replace_letters_in_word(word, current_word, guess):
    for index, x in enumerate(current_word):
        if x == "_":
            if word[index] == guess:
                current_word[index] = guess
    return current_word


def print_word(word):
    print("\nWord: {0}".format(" ".join([x for x in word])))


def game_over_replay():
    print("\n\nGame Over...")
    retry = ""

    while retry != "y" and retry != "n":
        retry = input("Do you wish to retry(y/n)")[0].lower()

    if retry == "y":
        return True
    else:
        return False


def clear_window():
    print('\n' * 100)


def play_game(word):
    print("[DEBUGGING PURPOSES] Secret word = {0}".format(word))
    guessed_letters = ""
    tries = 6
    # Current word with guessed letters
    current_word = ["_" for x in word]

    while tries > 0:
        # Print my sexy ASCII hangman guy
        draw_hangman(6-tries)

        print_word(current_word) # Yes, I do use a lot of functions
        print("Tries left: {0}".format(tries))
        print("Guessed letters: {0}".format(", ".join(guessed_letters)))

        guess = input("Guess a letter: ")[0].lower()
        # Check if the guessed letter is in word
        if guess not in guessed_letters:
            if guess in word:
                current_word = replace_letters_in_word(word, current_word, guess)
            else:  # If guess(Character) if not in the word
                tries -= 1

            guessed_letters += guess
        else:
            print("You already guessed that letter")

        # Check if the user won
        if check_if_win(current_word):
            print("\nCongratulations! You Won!")
            break

        time.sleep(0.5)
        clear_window()

if __name__ == "__main__":
    main()
