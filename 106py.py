import re

pattern1 = r"s.e"        # any character can come in place of dot
pattern2 = r"^s.e$"      # has to start with s and end with e
pattern3 = r"[aeiou]"    # has to start from any vowels
pattern4 = r"[A-Z][0-9]" # has to follow uppercase letter followed by a number
pattern5 = r"[^A-Z]"     # anything other than uppercase alphabets

if re.match(pattern1, 'see'):
    print("Match 1")
if re.match(pattern2,"she"):
    print("Match 2")
if re.match(pattern3,"afk"):
    print("Match 3")
if re.match(pattern4,"S9"):
    print("Match 4")
if re.match(pattern5,"hi"):
    print("Match 5")

# =======
# Result:
# ==============================================================================
# Match 1
# Match 2
# Match 3
# Match 4
# Match 5
# ==============================================================================
