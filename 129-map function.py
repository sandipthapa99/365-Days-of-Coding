myList = [2,3,5,7]
 
def square(myList):
    return myList * 2
 
list2 = list(map(square, myList))
print(list2)

# --------
# Result:
# ----------------------------------
# [4, 6, 10, 14]
# ----------------------------------