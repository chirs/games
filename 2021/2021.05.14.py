

def express():

    def split_cake(func, end):

        remainder = 1

        for i in range(1, end):
            remainder -= (remainder * func(i))

        return remainder

    friends = 1000000

    print(split_cake(lambda i: 1 / float(i+1), friends))
    print(split_cake(lambda i: 1 / float(i+1)**2, friends))
    print(split_cake(lambda i: 1 / float(2*i)**2, friends))


    

    



def classic():
    pass



class Veinte(object):
    """
    A game where you count to 20. 
    """

    options = [1,2,3,4]
    

    def __init__(players, limit=20):
        self.players = players
        self.limit = limit

    

    


def main():

    express()
    
        

if __name__ == "__main__":
    main()
