

from collections import Counter, defaultdict
import random




def classic():
    r1 = list(range(1, 9))
    r2 = list(range(1, 9))
    r3 = list(range(1, 9))

    random.shuffle(r1)
    random.shuffle(r2)
    random.shuffle(r3)    

    products = [a * b * c for (a, b, c) in zip(r1, r2, r3)]

    return min(products)





def main(times):

    answer = 1
    
    for e in range(times):
        c = classic()
        if c > answer:
            answer = c

    return answer



if __name__ == "__main__":

    d = defaultdict(int)
    
    for e in range(1000):
        d[main(10000)] += 1

    print(sorted(d.items()))
    
