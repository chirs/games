


def express(tickets):
    """
    you go back in time to win the $10m lottery
    so do 9 other people; they buy 1 ticket each.
    how many tickets should you buy to maximize winnings?
    1  -> $0999999
    11 -> $5499989
    """

    prize = 10000000
    all_winners = tickets + 9

    cut = prize * (tickets / all_winners)

    net = cut - tickets



    return net



def classic():
    """
    this one is about a doppelganger.
    I don't really care too much.
    """



def main():

    # write generic search function here

    previous = -1
    
    for i in range(1000000):
        r = express(i)

        if r < previous:
            return i

        previous = r
            

def binary_search():
    pass



if __name__ == "__main__":
    print(main())

    


    




    
