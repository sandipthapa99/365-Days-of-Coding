# sum of first n numbers using eval func
def sum(n):
    nums = range(1,n+1)
    e = eval("+".join([str(i) for i in nums]))
    return e
print(sum(5))
# returns sum of numbers upto 5

# --------
# Result:
# ----------------------------------------------
# 15
# ----------------------------------------------