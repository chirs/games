
def express():
    # 100 marbles
    # quantities are a, b, c
    # a + b + c = 1
    # 6 * a * b * c = .2 = 1/5
    # a * b * c = 1 / 30
    # 30 = 2 * 3 * 5
    # 20, 30, 50 marbles in each bag?
    # .2 * .3 * .5 * 6 = .18...
    # .3 * .3 * .4 = 6
    # .25 * .3 * .45 = 6
    # ## ##
    # 1 / 30 = 10 / 300

    print('hello')

    for e in range(101):
        for f in range(101):
            for g in range(101):
                x = (6 / 100000000)
                r = e * f * g * x
                if r > .19999:
                    if r < .20001:
                        print("{} {} {}".format(e,f,g))


def classic():
    pass


                        
#express()


def milk():
    # I need 75 ml of milk
    # I have 60 ml cup, 85 ml cup

    # fill 85
    # pour into 60; 25 remain
    # empty 60
    # move 25 from 85 to 60
    # fill 85
    # pour 35 ml into 60
    # 50 remain in 85
    # fill 60
    # pour into 85...
    # i give up

    pass


    
