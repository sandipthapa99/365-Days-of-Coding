import keyword

key = input("Your string:")

if keyword.iskeyword(key):
    print(key+ " is a python keyword")
else:
    print(key + " is not a python keyword")


# ======
# Input:
# ===========================================
# '''
# for
# forif
# elif
# '''
# =======
# Result:
# ===========================================
# '''
# for is a python keyword
# forif is not a python keyword
# elif is a python keyword
# '''
# ===========================================
# '''