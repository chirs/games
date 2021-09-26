
import math


### centrifuge

def setup():
    points = range(1, 13)
    pi_points = [math.pi * e for e in points]
    xs_ys = [(math.sin(e / 6), math.cos(e / 6)) for e in pi_points]

    return dict(zip(points, xs_ys))


mapping = setup()


def check_balance(positions):

    xys = [mapping[e] for e in positions]

    x_sum = sum([x for x,y in xys])
    y_sum = sum([y for x,y in xys])

    return (x_sum, y_sum)


def centrifuge():


    mapping = setup()

    #print([mapping[e] for e in [1,7]])

    #print(check_balance([1,7]))
    #print(check_balance([1,5,9]))
    #print(check_balance([3,6,9,12]))

    print(check_balance([11,12,1,4,5,7,8]))

    print(check_balance([11,12,1,4,5,7,8]))        



def main():

    print('hello')

    i = 267751
    
    while i > 1:
        print(i)
        i -= 1
        i = math.ceil(i / 2.0)
        

    



if __name__ == "__main__":
    main()
