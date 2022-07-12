

import math
import random





def express():
    """
    Surface of a sphere the same numeral as its volume
    """
    # 4 * pi * r**2 == 4/3 * pi * r**3
    # 3 * r**2 == r**3
    # r == 3

    # 4-d hypersphere version
    #

    # Interesting
    # Vn+1 = Sn / n+1

    

    


def gamma_function():
    """
    For any positive integer n, G(n) = (n-1)!
    """
    pass
    


def n_ball_volume(radius, n):
    """
    Radius of an n-dimensional ball (eg sphere)
    """

    nx = n / 2.0
    numerator = math.pi ** nx
    denominator = gamma_function(nx+1)
    return radius**n * (numerator / denominator)


def n_ball_surface_area(radius, n):
    pass

def classic_monte_carlo():
    """
    Squid game guess the right square. 
    18 total choices. 
    16 competitors. 
    """

    # This is too imprecise for the necessary result.
    # Answer is 7.000076294

    n = 100000
    s = 0
    for i in range(n):
        s += classic_subroutine()
        
    return s / float(n)


def classic_subroutine(competitors=16, steps=18):

    while competitors:
        if steps == 0:
            return competitors

        c = random.choice([0, 1])

        steps -= 1
        if c:
            competitors -= 1

    return 0
        
    
    


def main():
    print(express())
    print(classic())


if __name__ == "__main__":
    main()
