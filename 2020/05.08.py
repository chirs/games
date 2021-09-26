

import itertools
import random

domino_list = [
    (0,0),
    (0,1),    
    (0,2),
    (0,3),    
    (0,4),
    (0,5),    
    (0,6),
    (1,1),
    (1,2),
    (1,3),
    (1,4),
    (1,5),
    (1,6),
    (2,2),
    (2,3),
    (2,4),
    (2,5),
    (2,6),            
    (3,3),
    (3,4),
    (3,5),
    (3,6),            
    (4,4),
    (4,5),
    (4,6),            
    (5,5),
    (5,6),
    (6,6),
    ]



def q1():
    choice = random.choice(domino_list)
    is_double = (choice[0] == choice[1])
    return is_double


def q2():
    choice = random.choice(domino_list)
    is_double = (choice[0] == choice[1])
    reveal_side = random.choice(choice)
    if reveal_side == 6:
        return is_double
    else:
        return None



def monte_carlo(func, trial_attempts):

    trials_run = 0
    positives = 0

    for e in range(trial_attempts):
        result = func()
        if result is not None:
            trials_run += 1
            if result:
                positives += 1

    percentage = float(positives) / trials_run

    return trials_run, percentage


def main():

    for func in (q1, q2):
    
        t, p = monte_carlo(func, 1000000)
        print(t)
        print(p)
        print()

if __name__ == "__main__":
    main()

            
        
        
        
        
        
    








