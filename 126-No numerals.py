dict = {'1':'one','2':'two','3':'three','4':'four','5':'five',
        '6':'six','7':'seven','8':'eight','9':'nine','0':'zero',}

text = input("Original text: ")
myList = text.split()

for words in myList:
    if words in dict:
        text = text.replace(words,dict[words])
print(text)

# ------
# Input:
# ----------------------
# 1 apple and 2 oranges
# ----------------------
# Result:
# --------------------------
# one apple and two oranges
# --------------------------