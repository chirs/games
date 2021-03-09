
import math


def express():

    # 4**3 = 64 possible sequences
    
    # yes: 

    # ppp, nnn, ddd, qqq

    # pnn
    # pdd, ndd
    # pqq, nqq, dqq

    # no: 

    # pnd, pnq, dnq
    # 
    

    
    pass




def check_game(n):

    # 200 games, 800 at bats
    # 800 * .2 = 160

    at_bats = n * 4

    nearby = at_bats * (n / 1000.0)

    below = int(math.floor(nearby))
    above = int(math.ceil(nearby))

    #if n == 249:
    #    import pdb; pdb.set_trace()


    if int(round(1000 * below / at_bats)) == n:
        return True

    if int(round(1000 * above / at_bats)) == n:
        return True

    return False



def classic():

    impossible_games = [e for e in range(1, 1001) if not check_game(e)]
    
    return impossible_games



def main():
    print(classic())


if __name__ == "__main__":
    main()


