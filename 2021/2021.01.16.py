

from collections import defaultdict
from itertools import product
from math import floor, ceil



### flutes


def flutes_integer():

    peak = 100
    current = 0
    step = .01

    d = defaultdict(int)

    #for i in range(100):
    while current < 100:
        i = floor(current)
        current += step
        
        for guess in range(i+1):
            d[guess] += guess
            
    for i in range(100):
        print("{}: {}".format(i, d[i]))


prime_factorizations = [
    (2**6, 3**4, 5, 7**3), # 14 -> 10 -> 4; 9, 9, 8, 8
    (2**7, 5**2, 7**2), # 11 -> 8, 4, 2, 2 or 4, 4, 4, 2
    (2, 3**4, 7**3), # 8
    ]


def filter_number(hundreds, tens, ones):

    if hundreds in []:
        return False
    
    if tens in (3, 6, 9):
        return False

    if ones in (4, 5, 8):
        return False

    return True
    

def sudoku():

    d = defaultdict(list)
    keys = set([294, 216, 135, 98, 112, 84, 245, 40])
    
    for i in range(100, 1000):
        hundreds, tens, ones = split_number(i)
        product = hundreds * tens * ones
        if product in keys and filter_number(hundreds, tens, ones):
            d[product].append(i)

    #for key, value in d.items():
    #    print("{}: {}".format(key, value))

    get_answer(d.values())

    #print(prod([len(e) for e in d.values()]))

        
def split_number(n):
    return [int(e) for e in str(n)]


def get_answer(lsts):

    get_places = lambda l, i: [int(str(e)[i]) for e in l]
    
    for group in product(*lsts):
        hundreds = get_places(group, 0)
        tens = get_places(group, 1)
        ones = get_places(group, 2)

        if prod(hundreds) == 8890560 and prod(tens) == 156800:
            #print(prod(ones))
            print(group)

        


def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p



options = """
40: [158, 185, 245, 254, 425, 452, 518, 524, 542, 581, 815, 851]
84: [267, 276, 347, 374, 437, 473, 627, 672, 726, 734, 743, 762]
98: [277, 727, 772]
112: [278, 287, 447, 474, 728, 744, 782, 827, 872]
135: [359, 395, 539, 593, 935, 953]
216: [389, 398, 469, 496, 649, 666, 694, 839, 893, 938, 946, 964, 983]
245: [577, 757, 775]
294: [677, 767, 776]
"""


def main():
    #flutes_integer()
    sudoku()
        


if __name__ == "__main__":
    main()
        
        
        
    
