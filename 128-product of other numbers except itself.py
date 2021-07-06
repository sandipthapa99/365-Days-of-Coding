
# Given an array of integers, return a new array such that each element at
# index i of the new array is the product of all the numbers in the original
# array except the one at i
# For example, if the input was [1, 2, 3, 4, 5], the expected output would
# be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expect output
# would be [2, 3, 6]

import math
list1 = [2,3,5,7]
list2 = [2,0,3]
list3 = [0,0]

def func(ls):
    result = []
    for i in range(len(ls)):
        start = ls[0]
        ls.remove(ls[0])
        prod = math.prod(ls)
        ls.append(start)
        result.append(prod)
    return result

print(func(list1))
print(func(list2))
print(func(list3))

# --------
# Result:
# ----------------------------
# [105, 70, 42, 30]
# [0, 6, 0]
# [0, 0]
# ----------------------------