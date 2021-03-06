import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 
                160000, 230000, 280000, 290000, 300000, 500000, 
                420000, 100000, 150000, 280000])

mean = np.mean(data)
sd = np.std(data)
x = 0

for y in data:
   if y >= (mean-sd) and y <= (mean+sd):
         x = x + 1
result = (x / len(data))*100
print (str(result) + '%')

# =======
# Result:
# =================================================================
# 62.5%
# =================================================================