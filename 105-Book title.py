file = open("books.txt", "r")

#your code goes here
lines = file.readlines()
for line in lines:
    line = line.replace('\n','')
    print (line,":",line[0]+str(len(line)))
file.close()


# Result:
# ==========================================================
# Rich Dad Poor Dad : R17
# Harry Potter : H12
# Alchemist : A9
# ==========================================================