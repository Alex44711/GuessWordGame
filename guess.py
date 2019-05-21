"""
# guess.py will represent the game itself(including the menu)
@Description of guess game:
Running guess.py start the guess game.
If choose l, the user can guess the letter one by one
If choose g, the user can guess the word
If choose t, it means the user give up this round, the answer will present.
If choose q, the game will be ended, and shows the statistical information.

Each incorrect guess when choose l and g, the number of bad guess will add one,
when choose t, the uncovered letter will be count to the missed letter,
If guess success, the score of each round will be the sum of each letter and minus 0.1*(the number of bad guesses)
If give up one word, the score will be calculated by the (score of covered letter - score of uncovered) minus 0.1*
( the number of bad guesses)
when choose q, when bad guess is 0 and missed letter is 4, word score will be 0, otherwise calculate the score as the
same way as tell me.
If the user got the right word, and the bad guesses time less than 10 times, score will be large than 0, equal 10 times,
score will be 0, large than 10 times, word score small than.
"""
import stringDatabase
import game


def get_random_word():
    """
    get the random_word from stringDatabase.py
    :return: a four letter random word
    """
    return stringDatabase.get_random_word()


def get_input_choice():
    """
    get the input_choice from stringDatabase.py
    :return: one letter choice
    """
    return stringDatabase.get_input_choice()


def get_input_letter():
    """
    get yhe input guessed letter from stringDatabase.py
    :return: one guessed letter
    """
    return stringDatabase.get_input_letter()


def get_guess_word():
    """
    get the guess word from stringDatabase.py
    :return: the guess word
    """
    return stringDatabase.get_guess_word()


def start_game():
    """
    start the guess game, show the start print
    """
    print("** The great guessing game **\n")
    # print("Current guess: " + random_word)


def replace_word(string, p, c):
    """
    use the right guessed letter replace the current "-" in the right location
    :param string: current_word
    :param p: index of the right guessed letter
    :param c: right guessed letter
    :return: word after replacement
    """
    new_name = []
    for s in string:
        new_name.append(s)
    new_name[p] = c
    return "".join(new_name)


def print_each_game():
    """
    get the static_information from game.py
    print the information of each round and format the output
    """
    wait_list = game.get_static_info()
    for each_line in wait_list:
        if each_line[0] == 0:
            break
        for index, each_item in enumerate(each_line):
            print(each_item, end=format_space(index, each_item))


def format_space(index, each_item):
    """
    control the space between two item in one line
    return the number of space
    :param index:
    :param each_item:
    :return:
    """
    if index == 0:
        return " "*(4-len(str(each_item))+7)
    elif index == 3:
        return " "*(11-len(str(each_item))+7)
    elif index == 4:
        return " "*20
    elif index == 1:
        return " "*7
    elif index == 2:
        return " "*6


def print_total_score():
    """
    calculate the total score of one game
    :return: the format total score
    """
    total_score = 0
    for each_information in statistics_information:
        total_score += float(each_information[5])
        if each_information[0] == 0:
            break
    return "{:.2f}".format(total_score)


def success_guess(res):
    """
    check if user guess the word correct
    :param res: the current word
    :return: result of guess
    """
    if res.count("-") == 0:
        return True
    else:
        return False


keep_game = True
game_times = -1
statistics_information = game.get_static_info()
while keep_game:
    random_word = get_random_word()
    start_game()
    game_times += 1
    statistics_information[game_times][0] = game_times+1
    statistics_information[game_times][1] = random_word
    guess_result = "----"
    print("Current guess:", guess_result)
    bad_guesses = 0
    while True:
        print("g = guess, t = tell me, l for a letter, and q to quit")
        choice = get_input_choice()
        if choice == "l":
            input_letter = get_input_letter()
            if input_letter in random_word:
                print("******************************")
                print("you found", random_word.count(input_letter), "letters !!!!!!!!!!!!!!")
                print("******************************\n")
                for inx, each_word in enumerate(random_word):
                    if input_letter == each_word:
                        guess_result = replace_word(guess_result, inx, input_letter)
                print("Current Guess:", guess_result)
            elif input_letter not in random_word:
                bad_guesses += 1
                statistics_information[game_times][3] = bad_guesses
                print("******************************")
                print("You cannot even guess one letter! Try again!")
                print("******************************\n")
                print("Current Guess:", guess_result)
            if success_guess(guess_result):
                no_count_missed = game.calculate_success_score(random_word)
                no_format = no_count_missed*(1-statistics_information[game_times][3]*0.1)
                statistics_information[game_times][5] = "{:.2f}".format(no_format)
                statistics_information[game_times][4] = 0
                statistics_information[game_times][2] = "Success"
                print("******************************")
                print("Congratulations! You got the correct word\n\n")
                break
        if choice == "q":
            statistics_information[game_times][2] = "Quit it"
            statistics_information[game_times][3] = bad_guesses
            statistics_information[game_times][4] = game.count_guessed_word(guess_result)
            if statistics_information[game_times][3] == 0 and statistics_information[game_times][4] == 4:
                statistics_information[game_times][5] = 0
            else:
                no_count_missed = game.calculate_quit_score(random_word, guess_result)
                no_format = no_count_missed * (1 - statistics_information[game_times][3] * 0.1)
                statistics_information[game_times][5] = "{:.2f}".format(no_format)
            # no_count_missed = game.calculate_quit_score(random_word, guess_result)
            # no_format = no_count_missed*(1 - statistics_information[game_times][3] * 0.1)
            # statistics_information[game_times][5] = "{:.2f}".format(no_format)
            keep_game = False
            print("Correct answer is:", random_word)
            # show statistics
            game.print_statistics()
            print_each_game()
            print("Total score is:", print_total_score())
            break
        if choice == "g":
            print("Current Guess:", guess_result)
            input_word = get_guess_word()
            if input_word == random_word:
                no_count_missed = game.calculate_success_score(random_word)
                no_format = no_count_missed * (1 - statistics_information[game_times][3] * 0.1)
                statistics_information[game_times][5] = "{:.2f}".format(no_format)
                # statistics_information[game_times][4] = game.count_guessed_word(guess_result)
                statistics_information[game_times][4] = 0
                statistics_information[game_times][2] = "Success"
                print("******************************")
                print("You got the right word, Congratulations!\n")
                break
            else:
                bad_guesses += 1
                statistics_information[game_times][3] = bad_guesses
                print("******************************")
                print("Guess again!\n")
        if choice == "t":
            statistics_information[game_times][2] = "Gave up"
            statistics_information[game_times][4] = game.count_guessed_word(guess_result)
            no_count_missed = game.calculate_quit_score(random_word, guess_result)
            no_format = no_count_missed * (1 - statistics_information[game_times][3] * 0.1)
            statistics_information[game_times][5] = "{:.2f}".format(no_format)
            print("******************************")
            print("Little bit tired? have a rest and keep guess")
            print("Correct answer is:", random_word + "\n")
            print("******************************")
            break



