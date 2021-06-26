import numpy as np

one_dim = np.array([2])
two_dim = np.array([[4,7],[11,13]])
three_dim = np.ones((3,3))

print("1-Dim:",one_dim)
print("2-Dim:",two_dim)
print("3-Dim:",three_dim)
print(np.add(one_dim,two_dim))
print(np.add(one_dim,three_dim))

# =======
# Result:
# ====================================
# 1-Dim: [2]
# 2-Dim: [[ 4  7]   
#         [11 13]]
# 3-Dim: [[1. 1. 1.]
#         [1. 1. 1.]       
#         [1. 1. 1.]]   

# [[ 6  9]
#  [13 15]]

# [[3. 3. 3.]
#  [3. 3. 3.]
#  [3. 3. 3.]]
#  ====================================