import numpy as np

x = np.arange(1, 7)
print(x)
y = x.reshape(3, 2)
print(y)

z = np.array([[1,2],[2,3],[4,5]])
a = z.reshape(6)
b = z.flatten()
print(a)
print(b)

# =======
# Result:
# ==================================
# [1 2 3 4 5 6]
# [[1 2]
#  [3 4]
#  [5 6]]
# [1 2 2 3 4 5]
# [1 2 2 3 4 5]
# ==================================