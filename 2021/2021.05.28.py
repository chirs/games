



def express():

    # 30 * 162 = 4860 games
    # odds of a perfect game = x
    # y = 1-x
    # y ** 4860 = .5
    y =  .5 ** (1 / float(30*162))
    x = 1 - y

    obp = 1 - (x ** (1 / 27.0))

    return obp
    


def classic():
    

    

    
