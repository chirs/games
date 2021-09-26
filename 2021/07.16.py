

def express():
    """
    I have three dogs: Fatch, Fetch and Fitch. 
    Yesterday, I found a brown 12-inch stick for them to play with. 
    I marked the top and bottom of the stick and then threw it for Fatch. 
    Fatch, a Dalmatian, bit it in a random spot — leaving a mark — and returned it to me. 
    In her honor, I painted the stick black from the top to the bite and white from the bottom to the bite.

    I subsequently threw the stick for Fetch and then for Fitch, each of whom retrieved the stick by biting a random spot. 
    What is the probability that Fetch and Fitch both bit the same color (i.e., both black or both white)?
    """

    pass

    # Fatch selects point p between 0 and 1.
    # Odds of dogs 2, 3 selecting the same spot are p**2 + (1-p)**2
    # Odds of selecting different spot are 2p(1-p) = 2p - 2p**2
    # double check...
    # suppose p = .4
    # odds of same side = .16 + .36 = .52
    # odds of other side = .8 * (.6) = .48
    # suppose p = .2
    # odds are .04 + .64 = .68
    # .1 = .01 + .81 = .82

    total = 0

    for i in range(0, 1001):
        total += .0000001 * (i**2 + (1000-i)**2)
        

    # seems to be 2 / 3 but...why?
    print(total / 100)


def classic():

    """
    Italy defeated England in a heartbreaking (for England) European Championship that came down to a penalty shootout. 
    In a shootout, teams alternate taking shots over the course of five rounds. 
    If, at any point, a team is guaranteed to have outscored its opponent after five rounds, the shootout ends prematurely, even if each side has not yet taken five shots. 
    If teams are tied after five rounds, they continue one round at a time until one team scores and another misses.

    If each player has a 70 percent chance of making any given penalty shot, then how many total shots will be taken on average?
    """

    odds_3 = 2 * .7**3 * .3**3 ### End after three shots ~ 1.85%
    

    



    
    pass


    


def main():
    express()
    classic()
    

if __name__ == "__main__":
    main()
        
        



