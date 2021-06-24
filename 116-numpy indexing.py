import numpy as np

x = np.arange(1,10)
print(x)
print(x[:])
print(x[:5])
print(x[5:])
print(x[-3:])
print(x[:-1])

# Conditional indexing
print(x[x>4])
print(x[(x>5) & (x%3==0)])

# =======
# Result:
# ==========================
# [1 2 3 4 5 6 7 8 9]
# [1 2 3 4 5]
# [6 7 8 9]
# [7 8 9]
# [1 2 3 4 5 6 7 8]
# [5 6 7 8 9]
# [6 9]
# ==========================