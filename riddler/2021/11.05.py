




def express():
    """
    A group of 101 people join μετα, and each person has a random, 50 percent chance of being friends with each of the other 100 people. Friendship is a symmetric relationship on μετα, so if you’re friends with me, then I am also friends with you.

    I pick a random person among the 101 — let’s suppose her name is Marcia. On average, how many friends would you expect each of Marcia’s friends to have?

    """
    # I don't see how this can be anything but 50.
    # Perhaps we're imagining a case where each person friends 50% of people.
    # So it doubles back.
    # In that case, there's the initial 50.
    # Plus of the non-friended 50, each has a 50% chance of being friends.
    # So 75.
    # But really 50. (lazy question?)



def classic():
    """
    """



def main():
    express()
    classic()


if __name__ == "__main__":
    main()


