

# https://fivethirtyeight.com/features/can-you-find-the-best-dungeons-dragons-strategy/

"""
How to make this better?

distributions
understand the reason

probabilistic approach?

"""


import itertools
import random
from collections import Counter


# all possibilities

def roll(sides):
    return range(1, sides+1)

def advantage(sides):
    return [max(a, b) for (a, b) in itertools.product(range(1, sides+1), repeat=2)]

def disadvantage(sides):
    return [min(a, b) for (a, b) in itertools.product(range(1, sides+1), repeat=2)]

def advantage_of_disadvantage(sides):
    return [max(a, b) for (a, b) in itertools.product(disadvantage(sides), repeat=2)]

def disadvantage_of_advantage(sides):
    return [min(a, b) for (a, b) in itertools.product(advantage(sides), repeat=2)]    


def average(lst):
    lst = list(lst)
    return sum(lst) / float(len(lst))


def expected_return():
    print(average(roll(20)))
    print(average(advantage(20)))
    print(average(disadvantage(20)))
    print(average(advantage_of_disadvantage(20)))                
    print(average(disadvantage_of_advantage(20)))


def percentage_return(number_needed, sides):

    names = ['r', 'ad', 'da']
    funcs = [roll, advantage_of_disadvantage, disadvantage_of_advantage]


    for name, func in zip(names, funcs):
        lst = list(func(sides))
        count = len([e for e in lst if e >= number_needed])
        percentage = count / float(len(lst))
        print(name + ": " + str(percentage))



def main():

    for e in range(1, 21):
        print("Needed: " + str(e))
        percentage_return(e, 20)
        print("")

    print()
    expected_return()        
        
        
    


"""

monte carlo approach

def roll(sides):
    return random.randint(1, sides)

def disadvantage(sides):
    return min(roll(sides), roll(sides))

def disadvantage(sides):
    return min(roll(sides), roll(sides))


def advantage_of_disadvantage(sides):
    return max(disadvantage(sides), disadvantage(sides))


def disadvantage_of_advantage(sides):
    return min(advantage(sides), advantage(sides))



def repeat(func, times):
    sum = 0
    for e in range(times):
        sum += func()

    return sum / float(times)





def main():


    print(repeat(lambda: roll(20), 1000000)) # 10.5

    print(repeat(lambda: advantage(20), 1000000)) # 13 5/6

    print(repeat(lambda: disadvantage(20), 1000000)) # 7 1/6

    # advantage of disadvantage    
    print(repeat(lambda: advantage_of_disadvantage(20), 1000000))  # 9.83 [9 5/6] [-2/3]

    # disadvantage of advantage
    print(repeat(lambda: disadvantage_of_advantage(20), 1000000))  # 11.16 [11 1/6] [+2/3]

"""


if __name__ == "__main__":
    main()
