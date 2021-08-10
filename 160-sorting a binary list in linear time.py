# Function to sort a binary list in linear time
def sort(Arr):
    # number of 0's
    no_zeros = Arr.count(0)
 
    # place all 0's from index 0
    i = 0
    while no_zeros:
        Arr[i] = 0
        no_zeros = no_zeros - 1
        i = i + 1
 
    # fill remaining indices with 1
    for j in range(i, len(Arr)):
        Arr[j] = 1
 
if __name__ == '__main__':
    ls = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
    sort(ls)
    print(ls)

# --------
# Result:
# ----------------------------------------
# [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
# ----------------------------------------