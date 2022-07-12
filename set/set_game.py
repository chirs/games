import itertools


# colors: rgp  red, green, purple
# shapes: osd  oval, swiggle, diamond
# number: 123  1, 2, 3
# fill:   esl  empty, solid, lines





def check_set(cards):
    a, b, c = cards

    for c1, c2, c3 in zip(a,b,c):
        if not check_category(c1, c2, c3):
            return False

    return True


def check_category(c1, c2, c3):
    if c1 == c2 == c3:
        return True
    elif c1 != c2 and c2 != c3 and c1 != c3:
        return True
    return False



def find_sets(card_list):
    sx = set()
    for grouping in itertools.combinations(card_list, 3):
        if check_set(grouping):
            sx.add(grouping)

    return sx
            

board = [
    'gd3l',
    'ps3e',
    'po2e',
    'rs1l',
    'rd3e',
    'ps2e',
    'rd1l',
    'ro2l',
    'pd3e',
    'go3l',
    'rs2l',
    'gs3e',
    ]


def main():
    print(check_set(['ro1e', 'ro2e', 'ro3e']))
    print(check_set(['go1e', 'ro2e', 'po3e']))
    print(check_set(['go1e', 'rs2e', 'pd3e']))
    print(check_set(['ro1e', 'rs2e', 'pd3e']))


    #print(find_sets(['go1e', 'rs2e', 'pd3e', 'ps2e']))
    print(find_sets(board))




if __name__ == "__main__":
    main()
