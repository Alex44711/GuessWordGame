# maintain information about a specific game
statistics_information = [[0 for x in range(6)] for x in range(100)]


def get_static_info():
    """
    get the static info in statistics_information
    :return:  return the needed information
    """
    return statistics_information


def print_statistics():
    """
    print the titles of the information
    """
    print("Game       Word       Status       Bad Guesses       Missed Letters       Score")
    print("----       ----       ------       -----------       --------------       -----")
    # print_each_game()


def count_guessed_word(current_guess):
    """
    count the missed_letter
    :param current_guess: current_word
    :return: number of missed letter
    """
    count = 0
    for each_letter in current_guess:
        if each_letter == "-":
            count += 1
    return count


def dictionary(key):
    """
    find the corresponding frequency of each letter
    :param key: one lowercase letter
    :return: score of each letter
    """
    # print("key", key)
    dict1 = {"a": 8.17,
             "b": 1.49,
             "c": 2.78,
             "d": 4.25,
             "e": 12.70,
             "f": 2.23,
             "g": 2.02,
             "h": 6.09,
             "i": 6.97,
             "j": 0.15,
             "k": 0.77,
             "l": 4.03,
             "m": 2.41,
             "n": 6.75,
             "o": 7.51,
             "p": 7.51,
             "q": 0.10,
             "r": 6.33,
             "s": 6.33,
             "t": 9.06,
             "u": 2.76,
             "v": 0.98,
             "w": 2.36,
             "x": 0.15,
             "y": 1.97,
             "z": 0.07,
             "-": 0}
    return dict1[key]


def calculate_quit_score(random_word, current_guess):
    """
    when user gave up this round, calculate their score
    :param random_word: the random_word from database
    :param current_guess: the current_guess word
    :return: the score they get
    """
    word_score = 0
    guess_score = 0
    for each_letter in random_word:
        word_score += dictionary(each_letter)
    for each_guess in current_guess:
        guess_score += dictionary(each_guess)
    return 2*guess_score-word_score


def calculate_success_score(random_word):
    """
    calculate the success guessed score
    :param random_word: the random_word from database
    :return: the score of this word
    """
    word_score = 0
    for each_letter in random_word:
        word_score += dictionary(each_letter)
    return word_score
