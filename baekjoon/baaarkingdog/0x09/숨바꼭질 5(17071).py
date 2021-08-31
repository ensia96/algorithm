import collections as c
n, k = map(int, input().split())
m = int(5 * 10e4)
l = [0] * (m + 1)
q, r = c.deque([(n, 0)]), -1

while q:
    p, t = q.popleft()
    x = k + (t*(1+t)//2)
    if p == x:
        exit(print(t))
    if x > m:
        break
    for a in [p-1, p+1, p*2]:
        if a == x + t + 1:
            exit(print(t + 1))
        if 0 < a <= m:
            q.append((a, t+1))

print(r)
