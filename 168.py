# Function to remove adjacent duplicates characters from a string
def removeDuplicates(text):
    # list to check characters and later merge new
    chars = list(text)
    # previous char in text
    prev = None
    # indexing for character placement in list
    k = 0
 
    for item in text:
        if prev != item:
            # places only distinct character into the list
            chars[k] = item
            prev = item
            k = k + 1
    # Joins all the items of the list into string
    return ''.join(chars[:k])
 
 
if __name__ == '__main__':
    text = "SSSANNNDIIIP"
    result = removeDuplicates(text)
    print(result)

# --------
# Result:
# ----------------------------------------------------------
# SANDIP
# ----------------------------------------------------------