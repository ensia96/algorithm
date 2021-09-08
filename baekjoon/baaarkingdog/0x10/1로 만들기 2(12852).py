n = int(input())
d, p, l = [0]*(n+1), [0, 1]+[0]*n, []

for i in range(2, n+1):
    d[i] = d[i-1]+1
    p[i] = i-1
    if not i % 2 and d[i] > d[i//2]+1:
        d[i] = d[i//2]+1
        p[i] = i//2
    if not i % 3 and d[i] > d[i//3]+1:
        d[i] = d[i//3]+1
        p[i] = i//3
c = n
while 1:
    l += [c]
    if c == 1:
        break
    c = p[c]

print(d[n])
print(*l)
