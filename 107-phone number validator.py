import re

pattern = r"[9][0-9]{9}"
# Starts with 9,
# followed by 9 repitition of numbers between 0-9

num=input()
match = re.match(pattern,num)
if match and len(num)==10:
    print (num,"is Valid number.")
else:
    print (num,"is Invalid number.")