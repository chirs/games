

import random

"""
The problem:

* how to rotate a sphere?
* How to identify spots on a sphere [related?]

The algorithm

Increase the counter
Rotate a sphere to a random point
Mark a circle of radius 1.
Check whether the entire sphere has been marked. [HOW???]

"""



def func():
    s = Sphere()
    bites = 0

    while not s.is_eaten():
        s.rotate() # random
        if s.top_uneaten(): # is this check useful?
            s.mark()
        bites += 1

    return bites


class Sphere(object):

    def __init__(self)

        self.current_angle = (0, 0)
        self.bites = []


    def rotate(self):
        self.current_angle = (
            random.range(0, 2),
            random.range(0, 2),
            )


    def is_eaten(self):
        pass

    def top_uneaten(self):
        pass

    def mark(self):
        
    

    

    
        
        
    
    
