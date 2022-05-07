A = [int(input())for _ in ' '*int(input())]
M = 1000000009
n = max(A)
D = [[0]*4 for _ in ' '*-~n]
D[1] = [0, 1, 0, 0]
D[2] = [0, 0, 1, 0]
D[3] = [0, 1, 1, 1]
for i in range(4, n+1):
    D[i][1] = (D[i-1][2]+D[i-1][3]) % M
    D[i][2] = (D[i-2][1]+D[i-2][3]) % M
    D[i][3] = (D[i-3][1]+D[i-3][2]) % M
for a in A:
    print(sum(D[a]))
