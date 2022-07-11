n = int(input())
A = [*map(int, input().split())]
D = []
for a in A:
    l, r, t = 0, len(D)-1, 0
    while l <= r:
        m = (l+r)//2
        if D[m] < a:
            l = t = m+1
        else:
            r = m-1
    if t == len(D):
        D += a,
    D[t] = a
print(len(D))
