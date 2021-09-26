
import itertools


def express():

    return (q1(), q2())


def q1():    

    lst = list(itertools.product('LR', repeat=10))

    directions =  [e.count('L') - e.count('R') for e in lst] 
    north = [e for e in directions if e % 4 == 0]
    probability  = float(len(north)) / len(directions)

    return probability


def q2():    

    lst = list(itertools.product('LSR', repeat=10))

    print(len(lst))

    directions =  [e.count('L') - e.count('R') for e in lst]
    north = [e for e in directions if e % 4 == 0]

    print(len(north))
    
    probability  = float(len(north)) / len(directions)

    return probability



def monte_carlo():
    pass





def classic():
    pass


def main():
    print(express())
    classic()


if __name__ == "__main__":
    main()


