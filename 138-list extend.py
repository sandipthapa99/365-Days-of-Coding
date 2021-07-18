# List extend
A = [2,3]
B = [5,7]
C = A.extend(B)
print(C)
print(A)

# On extending list A with B, the elements of B are
# added to list A rather than creating new list
# so on printing C, we get None returned
# To get the result we have to print A as it is udated
# by the operation

# --------
# Result:
# --------------------------------------------------------
# None
# [2, 3, 5, 7]
# --------------------------------------------------------