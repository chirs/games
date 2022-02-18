


def calculate_power(cadence, resistance):
    return .05 * cadence * resistance



def express():

    p1 = 20 * 60 * .05 * .5 + 60 * 100 * .05 * .5
    p2 = 20 * 100 * .05 * .5 + 60 * 60 * .05 * .5

    print(p1)
    print(p2)

    # pretty sure the answer is just this: 140, 180

    return (p1, p2)



def classic():
    """
    Each ranger should spend as many weeks in the north as they do in the south.
    # Each ranger should spend the same number of weeks paired with each other ranger.
    # All rangers should move the same number of times over the course of the schedule. This includes potentially moving back to their starting assignment after the last week of the schedule.
    Exactly two rangers should switch locations each week.

    What is the shortest possible repeating schedule that meets the rangers’ conditions?
    """

    w1 = [(0,1),(2,3)]

    # this is a breadth-first search problem

    

    


def main():
    express()



if __name__ == "__main__":
    main()
