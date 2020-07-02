
from collections import defaultdict

states = [
    'alaska',
    'hawaii',
    'washington',
    'oregon',
    'california',
    'idaho',
    'nevada',
    'montana',
    'wyoming',
    'north dakota',
    'south dakota',
    'colorado',
    'arizona',
    'new mexico',
    'texas',
    'oklahoma',
    'kansas',
    'iowa',
    'minnesota',
    'missouri',
    'arkansas',
    'louisiana',
    'mississippi',
    'alabama',
    'florida',
    'georgia',
    'south carolina',
    'north carolina',
    'virginia',
    'maryland',
    'delaware',
    'pennsylvania',
    'new jersey',
    'new york',
    'connecticut',
    'rhode island',
    'massachusetts',
    'vermont',
    'new hampshire',
    'maine',
    'west virginia',
    'tennessee',
    'kentucky',
    'ohio',
    'indiana',
    'illinois',
    'michigan',
    'utah',
    'nebraska',
    'wisconsin',
    ]

state_letter_map = dict([(state, set(state)) for state in states])


def load_word_list():
    f = open('word.list.txt')
    s = f.read().split('\n')
    words = set(s)
    return words


def find_isolate(word, match_sets):
    matches = 0
    match = None

    word_letters = set(word)

    for state, state_letters in match_sets.items():
        if not word_letters.intersection(state_letters):
            if matches:
                return None
            else:
                matches += 1
                match = state

    return match


def build_isolate_map():

    d = defaultdict(list)
    
    word_list = load_word_list()
    for word in word_list:
        isolate = find_isolate(word, state_letter_map)
        if isolate:
            d[isolate].append(word)

    return d


def main():
    isolate_map = build_isolate_map()

    sorted_isolate_map = sorted(isolate_map.items(), key = lambda kv: len(kv[1]))

    for state, isolates in sorted_isolate_map:
        print(state)
        print(len(isolates))
        print('')
    

def problem1():

    word_list = sorted(load_word_list(), key = lambda k: -len(k))

    for word in word_list:
        isolate = find_isolate(word, state_letter_map)
        if isolate:
            print(word)
            print(isolate)
            return
    



        
if __name__ == "__main__":
    problem1()
    #main()
