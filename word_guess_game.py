import random


def get_player_name():
    """
    Get the player's name as input

    Returns:
        str: The player's name.
    """
    name = input("What's your name? ")
    return name


def choose_random_word():
    """
    Choose a random word from a predefined list of words.

    Returns:
        str: A randomly selected word.
    """
    words = [
        "banana",
        "elephant",
        "computer",
        "basketball",
        "butterfly",
        "rainbow",
        "waterfall",
        "octopus",
        "pineapple",
        "kangaroo",
        "xerox",
        "philantrophy",
        "fibonacci series",
    ]
    return random.choice(words)


def display_word(word, guesses):
    """
    Display the word with correctly guessed characters and underscores for missing characters.

    Args:
        word (str): The word to guess.
        guesses (str): The characters guessed by the player.
    """
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_ ", end=" ")


def play_game():
    """
    Play the word guessing game.
    """
    name = get_player_name()
    print("Good Luck, ", name)

    word = choose_random_word()
    print("Guess the characters")

    guesses = ""
    turns = 12

    while turns > 0:
        failed = 0

        display_word(word, guesses)

        if word == "".join([char if char in guesses else "_" for char in word]):
            print("\nCongratulations, you won!")
            print("The word is", word)
            break

        guess = input("\nGuess a character: ")

        if len(guess) != 1:
            print("Please enter only one character at a time.")
            continue

        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have", turns, "turns left")

        if turns == 0:
            print("You lose. The correct word was", word)



def main():
    """
    Main function to start the game.
    """
    play_game()


if __name__ == "__main__":
    main()
