import stringDatabase
# guess.py will represent the game itself(including the menu)


def get_random_word():
    return stringDatabase.get_random_word()


def get_input_choice():
    return stringDatabase.get_input_choice()


def get_input_letter():
    return stringDatabase.get_input_letter()


def get_guess_word():
    return stringDatabase.get_guess_word()


def start_game():
    print("** The great guessing game **\n")
    print("Current guess: " + random_word)


def replace_word(string, p, c):
    new_name = []
    for s in string:
        new_name.append(s)
    new_name[p] = c
    return "".join(new_name)


def success_guess(res):
    if res.count("-") == 0:
        return True
    else:
        return False


keep_game = True
while keep_game:
    random_word = get_random_word()
    start_game()
    guess_result = "----"
    print("Current guess:", guess_result)
    while True:
        print("g = guess, t = tell me, l for a letter, and q to quit")
        choice = get_input_choice()
        if choice == "l":
            input_letter = get_input_letter()
            if input_letter in random_word:
                print("you found", random_word.count(input_letter), "letters")
                for inx, each_word in enumerate(random_word):
                    if input_letter == each_word:
                        guess_result = replace_word(guess_result, inx, input_letter)
                print("Current Guess:", guess_result)
            elif input_letter not in random_word:
                print("You cannot even guess one letter! Try again!")
                print("Current Guess:", guess_result)
            if success_guess(guess_result):
                print("Congratulations! You got the correct word\n\n")
                break
        if choice == "q":
            keep_game = False
            print("Correct answer is:", random_word)
            # show statistics
            break
        if choice == "g":
            print("Current Guess:", guess_result)
            input_word = get_guess_word()
            if input_word == random_word:
                print("You got the right word, Congratulations!")
                break
            else:
                print("Guess again!")
        if choice == "t":
            print("Little bit tired? have a rest and keep guess")
            print("Correct answer is:", random_word + "\n")
            break





