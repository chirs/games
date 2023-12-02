
### For the riddler crossproduct series

import math
import itertools

from collections import Counter, defaultdict
from functools import reduce



def factor(n):
   if n == 1:
      return []
   try:
      for i in range(2, n+1):
         if n % i == 0:
            return [i] + factor(n // i)
   except:
      import pdb; pdb.set_trace()
      x = 5


# one_digit_factors = [factor(e) for e in range(10)]

possible_groupings = set([
      (), # 1, technically
      (2, ),
      (3, ),
      (2, 2),
      (5, ),
      (2, 3),
      (7),
      (2, 2, 2),
      (3, 3),
      (2, 5),
      ])


def possible_factor_groups(lst):

   # let's start with (2,)
   
   # let's start with (2, 2, 2, 2, 3, 5) = 240
   # We'll generate all the groups, and fail on the ones that don't clean us out

   groupings = itertools.product([0,1,2], repeat=len(lst))

   def create_sublists(grouping):
      d = defaultdict(list)
      for number, key in zip(lst, grouping):
         d[key].append(number)
      
      return [d[0], d[1], d[2]]

   def filter_sublist(sublist):

      for factor_group in sublist:
         if len(factor_group) == 0:
            pass
         else:
            product = reduce((lambda x, y: x * y), factor_group)
            if product > 9:
               return False

      return True

   raw_sublists = [create_sublists(g) for g in groupings]
   filtered_sublists = [e for e in raw_sublists if filter_sublist(e)]
   
   unduplicated_sublists = set([tuple(sorted([tuple(i) for i in e])) for e in filtered_sublists])
      
   return unduplicated_sublists
            

def problem():
   l = [280, 168, 162, 360, 60, 256, 126]
   for item in l:
      print(possible_factor_groups(factor(item)))

   l2 = [183708, 245760, 117600]
   for item in l2:
      print(possible_factor_groups(factor(item)))
      


   

def main():
   #print(factor(240))
   #print(possible_factor_groups(factor(240)))

   print(possible_factor_groups(1))

   #problem()
                          
   #print(list(all_combinations(factor(240))))
                     


if __name__ == "__main__":
   main()



      


 
   
   
