
from itertools import product, count
import time


def express():
    """
    Your challenge is to find starting whole numbers a, b and c so that 2023 is somewhere in their tribonacci sequence, a ≤ b ≤ c, and the sum a + b + c is as small as possible.
    """

    year = 2023    

    for n in count(1):
        tx = generate_triplets(n)
        for t in tx:
            if test_tribonacci(t, year):
                return t


def generate_triplets(n):


    l1 = [ (a,b) for (a,b) in product(range(n), repeat=2) if n-a-b>=0]
    l2 = [(a, b, n-a-b) for a, b in l1]
    return l2



def generate_tribonacci(a, b, c):
    
    while True:
        d = a+b+c
        yield d
        a, b, c = b, c, d


def test_tribonacci(triplet, target):
    a, b, c = triplet
    for e in generate_tribonacci(*triplet):
        if e < target:
            pass
        elif e == target:
            print(e)
            return True
        else:
            return False


def classic():
    pass


def christmas_match():
    """
    There are 20 people in the gift exchange. 
    In the first round, everyone writes down the name of a random person (other than themselves) and the names go in a hat. 
    Then if two people randomly pick each other’s names out of that hat, they will exchange gifts, and they no longer participate in the drawing.
    The remaining family members go on to round two. This continues until everyone is paired up.
    And yes, if exactly two people remain, they still go through the process of selecting each other, even though they know who their partner will be.
    On average, what is the expected number of rounds until everyone is paired up?
    """

    # So, with 2 people, odss are 50-50 you get a match, so you have 2.
    # This caveat sort of implies this question has a math result.
    # 4 people, abcd, can draw 4 * 3 * 2 = 24 different name-sets
    # the 6 where a draws a are automatically eliminated.
    # bacd, badc, bcad, bcda, bdac, bdca
    # cabd, cadb, cbad, cbda, cdab, cdba
    # dabc, dacb, dbac, dbca, dcab, dcba
    # Those are the options, so which ones are gonna produce 2 matches:
    # badc, cdab, dcba
    # one match? any permutation with two letters in place.
    # bacd, cbad, dbca
    # abdc, acbd, adcb
    # So for 4, you've got 3 options that match 4, and 6 that match 2. So 1/8 chance of 1, 1/4 chance of 1+2 = 3, 5/8 chance of try again. 
    # so it's sort of like generating a sequence of letters, using only transpositions.
    # up to 10, i guess, for a 20-person party.
    # and you can reason about that somehow
    # So what's the sum?
    # .625 is what we keep raising to.
    # .125 + .75 = .875 is the other part. 



def geometric_sum(a, r):
    if r >= 1:
        raise Exception

    return a / float(1-r)
    
    

def main():

    for e in generate_tribonacci(4,1,1):
        print(e)

    t = express()


if __name__ == "__main__":
    main()

    
