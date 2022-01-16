n = int(input())
P = [*map(int, input().split())]
d = int(input())
C = [[]for _ in ' '*n]
for i in range(n):
    if P[i] > -1:
        C[P[i]] += [i]
if P[d] > -1:
    C[P[d]].pop()
q = [d]
for d in q:
    q += C[d]
    C[d] = 1
print(sum(not c for c in C))
