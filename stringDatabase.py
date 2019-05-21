import random


# stringDatabase will be responsible for all dish I/O and check the valida of input
def get_random_word():
    """
    get a random four letters word from the four_letters.txt
    :return: a four letters word
    """
    word_list = []
    for lines in open("four_letters.txt"):
        for word in lines.split(" "):
            if len(word) == 5:
                word_list.append(word[0:4])
            else:
                word_list.append(word)
    return word_list[random.randint(0, len(word_list))]


def get_input_choice():
    """
    get the input choice and check the validation, if invalid, re-enter
    :return: a letter for choice
    """
    choice = input("Select one option:")
    while choice != "g" and choice != "t" and choice != "l" and choice != "q":
        print("Invalid choice, please select again!\n")
        choice = input("Select one option:")
    return choice


def get_input_letter():
    """
    If choice l, input guessed a English letter, if invalid, re-enter
    :return: a guessed letter
    """
    input_letter = input("Enter a letter:")
    while len(input_letter) != 1 or not input_letter.islower():
        print("Enter one single lower English letter, please enter again!\n")
        input_letter = input("Enter a letter:")
    return input_letter


def get_guess_word():
    """
    If choice g, input guessed letters, if the input invalid, re-enter
    :return: a guessed word
    """
    input_word = input("Enter the word you guess:")
    while len(input_word) != 4 or not input_word.islower():
        print("Remember, enter four letters word!")
        input_word = input("Re-enter the word you guess:")
    return input_word



