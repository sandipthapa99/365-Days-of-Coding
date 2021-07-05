from itertools import combinations

myList = []
n = int(input("Enter number of elements : "))

def func(myList):
    for i in range(0, n):
        element = int(input())
        myList.append(element) # adding the element
    print(myList)

    k = int(input("Sum value: "))

    #combination of list items
    comb = list(combinations(myList, 2))

    # checking if the sum of combination equals to k
    res = any(sum(i) == k for i in comb)

    return res

func(myList)

# ------
# Input:
# ------------------------------------------------------
# list -> [2,3,5,7]
# k -> 10
# ------------------------------------------------------
# Output:
# --------
# True
# ------------------------------------------------------

# Given a list of numbers, return whether any two sums to k.
# For example, given [2, 3, 5, 7] and k of 10, 
# return true since 3 + 7 is 10.