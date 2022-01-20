n = int(input())
P, C = [*map(int, input().split())], [[]for _ in ' '*n]
for i in range(n):
    if P[i] > -1:
        C[P[i]] += [i]
q = [int(input())]
for d in q:
    q += C[d]
    C[d] = 1
print(sum(not c for c in C))
