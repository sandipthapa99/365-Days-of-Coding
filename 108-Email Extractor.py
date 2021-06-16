import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
text = "Hello Connections, contact me at sandipthapa386@gmail.com"

match = re.search(pattern, text)
if match:
    print("e-mail:",match.group())
