n, m = int(input()), 8**8
A = [*map(int, input().split())]
D = [m]*n
D[0] = 0
for i in range(n):
    for j in range(A[i]+1):
        if i+j < n:
            D[i+j] = min(D[i+j], D[i]+1)
print(D[-1]if m-D[-1]else -1)
