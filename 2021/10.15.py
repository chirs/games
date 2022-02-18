


def express():
    """
    two evenly matched teams
    how long does the series last?
    """

    # 0 games = 1/2 ** 4 = 1/16
    # 1 games = 4 * 1/2 ** 5 = 1/8
    # 2 games = (5 * 2) * 1/2 ** 6 = 5/32
    # 3 games = (5 * 4) * 1/2 ** 7 = 5/32

    return 2 * ((4 * 1/16) + (5 * 1/8) + 6 * (5/32) + 7 * (5/32))


def classic():
    pass


def main():
    print(express())


if __name__ == "__main__":
    main()
    
