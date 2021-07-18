# lambda functionss

#  second lambda takes 1 as the value for x,
# which be used as the value of first x

a = (lambda x:x**3)((lambda x:x+2)(1))
print(a)

# --------
# Result:
# ----------------------------------------------
# 27
# ----------------------------------------------