# 3x3 matrix
A = [[2,3,5],
    [7,11,13],
    [17,19,23]]

# 3x2 matrix
B = [[29,31],
    [41,43],
    [53,59]]

# result will be 3x2
result = [[0,0],
         [0,0],
         [0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j] 

for r in result:
    print(r)

# =======
# Result:
# =============================================
# [446, 486]
# [1343, 1457]
# [2491, 2701]
# =============================================