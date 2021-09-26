


# unnecessary...i forgot      
def common_factors(l1, l2):
   common_elements = set(l1).intersection(set(l2))
   c1 = Counter(l1)
   c2 = Counter(l2)
   
   d = {}
   for key in common_elements:
      d[key] = min(c1[key], c2[key])
   return d
