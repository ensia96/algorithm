_, m = map(int, input().split())
T = [*map(int, input().split())]
s, e = 0, max(T)
while s < e:
    h = (s+e+1)//2
    if sum(max(0, t-h)for t in T) >= m:
        s = h
    else:
        e = h-1
print(s)
