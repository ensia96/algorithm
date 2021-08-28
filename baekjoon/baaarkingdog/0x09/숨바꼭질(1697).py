import collections as c

n, k = map(int, input().split())
q, v, l = c.deque([(n, 0)]), 0, [0] * (k + 1)

while q:
    if c == k:
        print(v)
        break
    c, v = q.popleft()
    for a in [c * 2, c + 1, c - 1]:
        if 0 < a <= k and not l[a]:
            l[a] = 1
            q.append((a, v + 1))
