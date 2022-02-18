
from collections import defaultdict


def crossword(height, width):
    return height * width



def get_english_word_list():
    f = open("words.txt")
    lines = f.read().split('\n')
    return lines



def words_by_length(word_list):

    d = defaultdict(set)
    
    for word in word_list:
        try:
            d[len(word)].add(word)
        except:
            import pdb; pdb.set_trace()

        x = 5

    return d



def possible_words(partial_word, word_list):
    # partial word is a list like ["", "a", "f", ""]

    words_dict = words_by_length(word_list)
    candidates = words_dict[len(partial_word)]
    possibles = set()


    def test_word(word):
        for char, test_char in zip(word, partial_word):
            if test_char:
                if char != test_char:
                    return False

        return True

    
    for word in candidates:
        if test_word(word):
            possibles.add(word)

    return possibles


def create_crossword(grid):
    # currently assuming no empty squares
    pass





def main():

    word_list = get_english_word_list()
    
    p = possible_words(["a", "l", None, None, None], word_list)
    print(p)
    


if __name__ == "__main__":
    main()
