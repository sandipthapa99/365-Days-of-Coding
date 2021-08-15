# Function to find a pair with the given difference in the list.
# This method does not handle duplicates in the list
def findPair(ls, diff):

    # for every element in the list
    for item in ls:
        # if pair with the given difference exists
        if item - diff in ls:
            print((item, item - diff))

 
if __name__ == '__main__':
 
    ls = [1,4,2,3,5,8]
    diff = 3
 
    findPair(ls, diff)

# --------
# Result:
# ------------------------
# (4,1)
# (5,2)
# (8,5)
# ------------------------