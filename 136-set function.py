# use of set() function

x = {1:0,0:1}
y = [1,[4,6,5,4],2]

print(list(set(y[x[0]]))[1])
# set function returns a set with distinct numbers
# in ascending order which is the tyoecasted into a list
# and the element at first index is accessed

# --------
# Result:
# --------------------------------------------------------
# 5
# --------------------------------------------------------