n = int(input())
A = [*map(int, input().split())]
C = [0]*7
for a in A:
    for i in range(7):
        if C[i]:
            C[(i+a) % 7] = 1
    C[a % 7] = 1
print(['NO', 'YES'][C[4]])
