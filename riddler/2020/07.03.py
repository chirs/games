
import itertools
import math
import time


### Swimming lanes


def lanes():
    # no real need for calculations here.

    # .2 chance someone picks the middle lane -> 3 people in the pool
    # .4 chance someone picks an interior lane -> 2 people in the pool
    # .4 chance someone picks an outside lane -> 2/3 chance of 3 and 1/3 chance of 2; average of 8/3
    # total expectation is .6 + .8 + 16/15 = 2.47 people on average? (2 7/15)

    # what about for n? 1 -> 1; 2 -> 1; 3 -> 5/3; 4 -> 2; 5 -> 2 7/15; 6 -> almost 3?

    pass

    

    
def centered_pentagonal_numbers():

    number = 1
    
    for i in itertools.count(start=1):
        yield number
        number += (i * 5)


def solve():
    for number in centered_pentagonal_numbers():

        n2 = (number - 1) / 2.0
        root = math.sqrt(n2)
        if abs(root - int(root)) < .01:
            print(n2)
            time.sleep(2)


if __name__ == "__main__":
    #for e in centered_pentagonal_numbers():
    #    pass
    
    solve()
    
