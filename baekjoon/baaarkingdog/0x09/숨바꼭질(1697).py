import collections as c

n, k = map(int, input().split())
q, l = c.deque([(n, 0)]),  [0] * (k + 1)
a, v = k, 0

while q:
    if c == k:
        a = min(a, v)
        break
    c, v = q.popleft()
    for m in [c * 2, c + 1, c - 1]:
        if 0 < m <= k and not l[m]:
            l[m] = 1
            q.append((m, v + 1))
print(a)
