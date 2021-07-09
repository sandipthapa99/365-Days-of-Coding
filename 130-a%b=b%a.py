def check(a,b):
    case1 = round(float((a/100)*b),2)
    case2 = round(float((b/100)*a),2)
    # print(case1, case2)
    if (case1 == case2):
        return True

check(3,5)
check(4,25)

# ------
# Result:
# --------------------------------------
# True
# --------------------------------------
