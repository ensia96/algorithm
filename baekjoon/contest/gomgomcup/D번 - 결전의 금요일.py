input()
C = [1]+[0]*6
for a in map(int, input().split()):
    c = [0]*7
    for i in range(7):
        if C[i]:
            c[(i+a) % 7] = c[i] = 1
    C = c
print(['NO', 'YES'][C[4]])
