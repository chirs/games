
import itertools


def format_express(l1, l2):

    s = '(' * len(l2) + str(l1[0])

    for symbol, number in zip(l2, l1[1:]):
        s += " " + symbol + " " + str(number) + ')'

    return s


def express(lst, target):

    unique_orderings = set(itertools.permutations(lst))

    result = []

    for ordering in unique_orderings:
        result.extend(express_subroutine(ordering, target))

    return result


def express_subroutine(numbers, target):
    """
    For a given ordering of numbers, try all combinations of expressions.
    """

    def sub2(numbers, funcs, target):
        """Apply the expressions and verify the result"""
        
        

        result = numbers[0]
        for number, func in zip(numbers[1:], funcs):
            result = func(result, number)

        return result == target

    def a(x,y): return x + y
    def s(x,y): return x - y
    def m(x,y): return x * y
    def d(x,y): return x / y    
    def e(x,y): return x ** y

    name_map = {
        a: '+',
        s: '-',
        m: '*',
        d: '/',
        e: '**',
    }

    l = [[a, s, d, m, e]] * (len(numbers) - 1)
    relations = list(itertools.product(*l))

    matches = []

    for relation in relations:
        if sub2(numbers, relation, target):
            try:
                t = (numbers, [name_map[e] for e in relation])
            except:
                import pdb; pdb.set_trace()
                
            matches.append(t)

    return matches
        

def ring_stack(element_count):
    """brute force ring stack solution"""
    # Don't try to run past 8 rings

    empty = "_"

    def subroutine(lst):
        """filter invalid rings"""
        
        for index, el in enumerate(lst):
            if el != empty:
                
                # eg a 1-diameter ring in the 2-spot
                if el < index: 
                    return False
                
                # eg a 3 should fall to the 3-spot unless it's blocked
                if el > index and lst[index+1] == empty:
                    return False

        return True
                    
    elements = list(range(element_count)) + [empty] * (element_count - 1) # rings plus empty slots
    combinations = itertools.combinations(elements, element_count) # all possible combinations of rings / empty slots

    permutations = []
    for c in combinations:
        permutations.extend(itertools.permutations(c))

    return [e for e in set(permutations) if subroutine(e)]


def numerical(n):

    return sum([i ** (n-i+1) for i in range(1, n+1)])
        


    
def main():

    #for e in express([2,3,3,4], 24):
    #    print(format_express(*e))

    #for e in range(1, 8): 
    #    print(len(ring_stack(e)))

    #for e in range(2, 9):
    #    print(len([l for l in ring_stack(e) if l.count("_") == 3]))

    for e in range(10):
        print(numerical(e))


if __name__ == "__main__":
    main()

    
