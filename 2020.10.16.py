
import random



def monte_carlo(func, trial_attempts):

    trials_run = 0
    positives = 0

    for e in range(trial_attempts):
        result = func()
        if result is not None:
            trials_run += 1
            if result:
                positives += 1

    percentage = float(positives) / trials_run

    return trials_run, percentage



def subprocess(competitors):
    results = sorted([random.random() for e in range(competitors - 1)])
    l1 = [0] + results
    l2 = results + [1]
    pairs = zip(l1, l2)
    for a, b in pairs:
        if b - a > .5:
            return True

    return False



def express():

    # 2 / 2
    # 3 / 4
    # 4 / 8
    # 5 / 16
    # 6 / 32
    # 7 / 64
    # 8 / 128

    
    for n in range(2, 10):
        yield monte_carlo(lambda: subprocess(n), 1000000)


def classic():
    pass


def main():

    #print(subprocess(2))
    
    for e in express():
        print(e)
    


if __name__ == "__main__":
    main()
