n, m = map(int, input().split())
D = [*map(int, input().split())]
for i in range(1, n):
    D[i] += D[i-1]
for _ in ' '*~-n:
    t, l, r = [*map(int, input().split())], [D[0]], [D[-1]]
    for i in range(m):
        l += max(l[-1], D[i])+t[i],
        r += max(r[-1], D[-i-1])+t[-1-i],
    D = [max(l[i+1], r[-i-1])for i in range(m)]
print(D[-1])
