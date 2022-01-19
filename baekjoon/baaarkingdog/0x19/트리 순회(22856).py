n = int(input())
R = [0]*(n+1)
for _ in ' '*n:
    a, b, c = map(int, input().split())
    R[a] = c+(c < 0)
q = [1]
for i in q:
    if R[i]:
        q += [R[i]]
print((n-1)*2-len(q)+1)
