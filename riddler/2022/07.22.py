

### Riddler Classic

"""
You and your team of cyclists are climbing a mountain with a constant gradient in the Tour de FiveThirtyEight. You make the climb single file, with one rider in front of the other. The first rider sets the tempo for the rest to follow — that is, until that first rider runs out of energy, or “cracks.” Upon cracking, a rider can no longer maintain the tempo and falls well behind any riders who still have some remaining energy.

When you begin the climb, there are eight riders on your team, and you start at the very back. The seven riders in front of you have exactly enough energy to make it up the entire climb, as long as they are not the first rider. Setting the tempo is hard work, and riding first in line is twice as exhausting as being one of the other riders.

At some point up the mountain, the first rider cracks. Then the next rider cracks, then the next. Eventually, the last rider in front of you cracks, leaving you to contend with the remaining portion of the mountain all on your own. What fraction of the mountain do you climb alone?
"""

def express():
    return "1/" + str(2**7)


"""
From Alec Stein, inspired by conversations with Jesse Zymet and Adam Greenberg, comes a puzzle that is sure to make you lose your marbles:

At the Riddler Marble Shop, there are four enormous bags of marbles for you to acquire. They are labeled “red,” “green,” “blue” and “assorted.” Being the purist that you are, you want to select two bags of marbles that are not assorted, and you’d settle for some combination of red, green or blue.

However, noticing your interest in the bags, the shopkeeper alerts you. “Buyer beware,” she warns. “Some jerk switched around the labels on all four bags. Right now, every single bag is incorrectly labeled.” To give you a chance of properly identifying the bags you would like, she has kindly allowed you to take two — and only two — marbles out of any of the bags, one at a time.

How can you guarantee that neither of the two bags you take is assorted?
"""

def classic():
    pass




if __name__ == "__main__":
    print(express())
    print(classic())
