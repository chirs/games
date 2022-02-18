

def collatz(n):
    if n % 2 == 1:
        return (3 * n) + 1
    else:
        return int(n / 2)



def q2():

    for i in range(300):
        r = collatz(collatz(collatz(collatz(collatz(i)))))
        if r > 999:
            print("{}: {}".format(i, r))




def shuffle(mapping, times=1, deck=None):

    if deck is None:
        deck = range(1, len(mapping) + 1)
    
    if times == 0:
        return deck

    d = dict(zip(mapping, deck))

    return shuffle(mapping, times-1, [e[1] for e in sorted(d.items())])


def q3():

    # 120

    mapping = [6,4,11,14,9,13,1,2,3,8,15,5,7,10,12]
    
    for times in range(200):
        s = shuffle(mapping, times)
        if s[0] == 1:
            print("{}: {}".format(times, s))




def q6():

    1

    # a**2 - b**2 = (a+b)(a-b) 
    # 9**2 - 8**2 = (17 * 1) = 17
    # 6**2 - 4**2 = 

    # first squares that have a gap greater than 100: 50, 51

    # so...all odds can be (eg 9**2 - 8**2) = 17; 10**2 - 9** 2 = 19, tc.
    # 9**2 - 7**2 = 32
    # 8**2 - 6**2 = 28
    # 7**2 - 5**2 = 24
    # so all multiples of 4, except 4...
    
    
    #squares = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,



def q5():

    s = set()

    for e in range(52):
        for f in range(52):
            diff = e**2 - f**2
            s.add(diff)


    for e in range(0, 101):
        if e not in s:
            print(e)
    
    


def main():
    #q2()
    q5()


if __name__ == "__main__":
    main()
