

import random
import math




def express():
    # make a chart, etc.

    
    initial = (0,0)

    d1 = 2 * math.pi * random.random()
    p1 = (math.sin(d1), math.cos(d1))

    d2 = 2 * math.pi * random.random()
    p2 = (p1[0] + math.sin(d2), p1[1] + math.cos(d2))

    return p2


def classic():
    


    


if __name__ == "__main__":
    for e in range(100):
        print(express())
