

from collections import Counter



def construct_staircase(string):

    possibiltiies = find_possibilities(string)

    for p in possibilities:
        construct_staircase(string)

    return strings


def find_possibilities(string)

    c = Counter(string)

    possibilities = []

    if c['a'] < 4:
        possibliities.append('a')

    if c['b'] < 3 and c['a'] > c['b']:
        possibilities.append('b')

    if c['c'] < 2 and c['b'] > c['c']:
        possibilities.append('c')

    if c['d'] < 0 and c['c'] > c['d']:
        possibilities.append('d')

    return possibilities
    
    




def blocks():

    pass

    # A [AB],
    # AA [AB]
    # AAA [AB]
    # AAAA [B]
    # AB [AC]
    # ABA [ABC]
    # ABC [A]

    # AAAA
    # AAAB
    # AABA
    # AABB
    # AABC
    # ABAA
    # ABAB
    # ABAC
    # ABCA

    # AAAAB
    # AAABB
    # AAABC
    # AABAA
    # AABAB
    # AABAC
    # AABBA
    # AABBC
    # AABCA
    # AABCB



def stack():
    # 2 ways to build an ABA stack:
    # AAB
    # ABA

    # how many ways to build the
    # no.
    pass



    


    
