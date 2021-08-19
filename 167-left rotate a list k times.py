# Function to left-rotate a list by one position
# Left rotate an element one at a time
def leftRotateByOne(A):
    first = A[0]
    # loop within elements except last one
    for i in range(len(A) - 1):
        A[i] = A[i + 1]
    # place first element into last index
    A[-1] = first
 
# Left rotate a list by k positions
def leftRotate(A, k):
    # invalid input case
    if k < 0 or k >= len(A):
        return

    # rotate k times
    for i in range(k):
        leftRotateByOne(A)
 
if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    k = 2
    leftRotate(A, k)
    print(A)

# --------
# Result:
# ------------------------------------------
# [3, 4, 5, 1, 2]
# ------------------------------------------