n = int(input())
C = [[*map(int, input().split())]for _ in ' '*n]
C += [C[0]]
x = y = z = 0
for i in range(n+1):
    x, y, z = min(y, z)+C[i][0], min(x, z)+C[i][1], min(x, y)+C[i][2]
t = min(C[0])
print(min(x-t, y-t, z-t))
