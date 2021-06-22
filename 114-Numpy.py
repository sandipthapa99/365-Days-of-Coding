import numpy as np
 
# 1 Dimensional
arr1 = np.array([2, 3, 5])
print("1 Dimensional Array: \n",arr1)
 
# 2 Dimensional
arr2 = np.array([[2, 3, 5],
                [7, 11, 13]])
print("\n2 Dimensional Array: \n", arr2)
 
# Creating an array from tuple
arr3 = np.array((2, 3, 5))
print("\nArray created using tuple:\n", arr3)

# =======
# Result:
# ============================================
# 1 Dimensional Array: 
#  [2 3 5]

# 2 Dimensional Array: 
#  [[2 3 5]
#  [7 11 13]]

# Array created using tuple:
#  [2 3 5]
#  ============================================