# nested functions
# function 1
def sub(x,y):
    return x-y
# function 2
def mult(x,y):
    return x*y
# making use of nested functions
def func(f1,f2,d):
    return(f1(f2(d+1,d),d))

func(mult,sub,7)

# --------
# Result:
# ----------------------------------------------
# 7
# ----------------------------------------------