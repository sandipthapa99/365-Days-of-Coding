from itertools import count, accumulate, takewhile
for i in count(3):
    print(i)
    if i>=11:
        break

print(list(i for i in range(8)))
nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x:x<=6,nums)))
