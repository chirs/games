



import random
import itertools






class Stack(object):
    # Jenga

    def __init__(self, centers=None):
        if centers:
            self.centers = centers
            self.blocks = len(centers)
        else:
            self.centers = [0]
            self.blocks = 1


    def add_block(self):

        self.blocks += 1
        
        previous_center = self.centers[-1]
        new_center = previous_center + random.random() - .5
        self.centers.append(new_center)

    @property
    def leftmost(self):
        return min(self.centers)

    @property
    def rightmost(self):
        return max(self.centers)


    def check_side_stability(self, extreme):
        
        above = False

        center_sum = 0
        center_count = 0
        
        for center in self.centers:
            if above:
                center_sum += center
                center_count += 1
                average_center = float(center_sum) / center_count
                if abs(average_center - extreme) > .5:
                    return False
            
            if center == extreme:
                above = True

        return True


    def check_stability(self):
        #if self.check_side_stability(self.leftmost) == False:
        #    return False

        if self.check_side_stability(self.rightmost) == False:
            return False        




def play_game():

    stack = Stack()
    for i in itertools.count(start=1):
        stack.add_block()
        if stack.check_stability() is False:
            return i



def main():

    games = 10000000
    results = sum([play_game() for game in range(games)])

    return results / float(games)

    

if __name__ == "__main__":
    print(main())
