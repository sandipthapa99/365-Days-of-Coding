import numpy as np

x = np.array([2,3,5,7,11,13,17,19,21,23,29])

print(np.mean(x))
print(np.median(x))
print(np.var(x))
print(np.std(x))

y = np.arange(1,10)
print(y*2)
print(y.sum())

# =======
# Result:
# ============================================
# 13.636363636363637
# 13.0
# 72.04958677685951
# 8.488202800172692
# [ 2  4  6  8 10 12 14 16 18]
# 45
# ============================================