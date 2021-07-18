

import itertools


def coin():
    # after one flip, no evidence
    # after two flips, a 50% chance vs. a 100% chance
    # after three flips, a 25% chance vs. a 100% chance
    # after four flips, a 12.5% chance vs. a 100% chance; evidence says 8/9 = 88.9% chance it is magic

    # FAILED
    # review prior probability / bayes

    for i in itertools.count():
        p = .5 ** i

        bayes = 1.0 / (1+p)
        if bayes > .99:
            return i



def spheres():
    # keep adding up cubes till it's possible to group them into 3 groups of equal weights

    for n in itertools.count(start=1):
        weights = list(range(1, n + 1))
        



def main():
    print(coin())


if __name__ == "__main__":
    main()
