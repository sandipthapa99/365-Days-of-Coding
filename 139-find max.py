# finding max number without using inbuilt function
myList = [2,3,5,7]
def max(nums):
    max = 0
    # compares every items with max value
    # if any item is greater than max,
    # update the max value
    for i in nums:
        if i > max:
            max = i
    return max
print(max(myList))

# --------
# Result:
# --------------------------------------------------------
# 7
# --------------------------------------------------------