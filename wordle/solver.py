
def get_word_list():
    f = open('wordle_word_list.txt').read()
    return f.split('\n')



def filter_incorrect_letters(incorrect_letters, word_list):
    s = set(incorrect_letters)
    return [word for word in word_list if not s.intersection(set(word))]


def filter_correct_position(t, word_list):
    letter, position = t
    return [word for word in word_list if word[position] == letter]

def filter_correct_positions(correct_tuples, word_list):
    l = word_list[:]
    for ct in correct_tuples:
        l = filter_correct_position(ct, l)
    return l


def filter_incorrect_position(t, word_list):
    letter, position = t
    return [word for word in word_list if letter in word and word[position] != letter]


def filter_incorrect_positions(incorrect_tuples, word_list):
    l = word_list[:]
    for it in incorrect_tuples:
        l = filter_incorrect_position(it, l)
    return l



def rg(t, word_list):
    wl = word_list[:]
    letters, position = t
    return [word for word in word_list if word[position] in letters]


def reverse_guess(tx, word_list):
    wl = word_list[:]
    for t in tx:
        wl = rg(t, wl)
    return wl






def filter_words(correct_positions, incorrect_positions, incorrect_letters, word_list):
    wl = word_list[:]
    wl = filter_correct_positions(correct_positions, wl)
    wl = filter_incorrect_positions(incorrect_positions, wl)
    wl = filter_incorrect_letters(incorrect_letters, wl)
    return wl


def reverse(correct_positions, reverses, incorrect_letters, word_list):
    wl = word_list[:]
    wl = filter_correct_positions(correct_positions, wl)
    wl = reverse_guess(reverses, wl)
    wl = filter_incorrect_letters(incorrect_letters, wl)
    return wl



def reconstruct(guesses):
    pass


def deconstruct_word(t):
    """
    eg ('paste', 'g__yg')
    """
    t = letter, colors
    correct = [(l, i) for ((l, c), i) in enumerate(t) if c == 'g']
    wrong_position = [(l, i) for ((l, c), i) in enumerate(t) if c == 'y']
    incorrect = [l for (l, c) in t if c == '_']
    return (correct, wrong_position, incorrect)

    


def main():
    word_list = get_word_list()
    excluded = 'bcdfghijkmnoqrstuvwxyz' # apple
    #l = filter_incorrect_letters(excluded, words)
    #l2 = filter_correct_positions([('a', 0)], l)
    #l3 = filter_incorrect_positions([('a', 1)], l)
    #l4 = filter_words([(e,4)],
    #return reverse_guess([, word_list)
    #return reverse([('e', 4)], [('aus', 0), ('pus', 1)], 'crn', word_list)
    #filter_words(
    #return reverse([('p', 0), ('a', 1), ('e', 4)], [('s', 3)], 'crn', word_list)

    #return filter_words([('e', 4)], [('a', 0), ('s', 1)], 'crnid', word_list)
    return filter_words([('e', 4), ], [('a', 0), ('p', 1), ('p', 2)], 'crnl', word_list)

    #return l4


if __name__ == "__main__":
    print(main())





            
