import itertools 
  
myList = [[2, 3], [5, 7], [11, 13]] 
  
res = list(itertools.chain.from_iterable(myList)) 
print(res)

# =======
# Result:
# =================================================
# [2, 3, 5, 7, 11, 13]
# =================================================