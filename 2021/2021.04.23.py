

from random import choice

from collections import defaultdict



def enigmerica_election():

    d = defaultdict(int)
    
    for e in range(80):
        d[choice('AB')] += 1

    d2 = defaultdict(int)

    for e in range(20):
        d2[choice('AB')] += 1

    d3 = {
        'A': d['A'] + d2['A'],
        'B': d['B'] + d2['B'],
        }

    if d['A'] > d['B']:
        early_winner = 'A'
    else:
        early_winner = 'B'

    if d['A'] > d['B']:
        late_winner = 'A'
    else:
        late_winner = 'B'

    return early_winner == late_winner



def main():
    attempts = 1000

    matches = 0

    for e in range(attempts):
        if enigmerica_election():
            matches += 1

    print(float(matches) / attempts)

    




if __name__ == "__main__":
    main()
        
    
    

    

    
        

    




    


    
