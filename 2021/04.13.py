

def pour(a, b):
    b += .5 * a
    a = .5 * a
    a += .5 * b
    b = .5 * b
    return (a, b)


def pour_a_lot(times):
    """
    Stabilizes at 2/3 (A+B) for the most recent pour, 
    1/3 (A+B) for the other.
    """
    a = b = 8
    for i in range(times):
        a, b = pour(a, b)
    return (a, b)



def paths():
    # 2 ** 12 = 4096 total paths
    # 25% chance first two squares will be impassable
    # 25% chance last two squares will be impassable
    # 7/16 chance at least one of first / last two squares impassable
    # most routes are length 4;
    # 6 routes of length 4
    # 4 routes of length 6
    # 2 routes of length 8

    # Routes:
    # 00-10-20-21-22
    # 00-10-11-21-22
    # 00-10-11-12-22
    # 00-01-02-12-22
    # 00-01-11-21-22
    # 00-01-11-12-22

    # 00-10-11-01-02-12-22
    # 00-10-20-21-11-12-22
    # 00-01-11-10-20-21-22
    # 00-01-02-12-11-21-22

    # 00-10-20-21-11-01-02-12-22
    # 00-01-02-12-11-21-20-21-22


    import itertools
    import random

    d = {}

    for path in itertools.product([0,1,2], [0,1,2]):
        direction = random.choice([0,1])
        d[path] = direction

    valid_paths = []


    # I can figure this one out but the code doesn't seem very nice.

        
        
    


    



def main():
    print(pour_a_lot(1000))


if __name__ == "__main__":
    main()
    
    
    
    
