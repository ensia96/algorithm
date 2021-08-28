import collections as c

n, k = map(int, input().split())
q, l = c.deque([(n, 0)]), [0] * (k + 2)

while q:
    c, v = q.popleft()
    if n == k or l[k]:
        print(l[k])
        break
    for m in [c - 1, c + 1, c * 2]:
        if 0 <= m < k + 2 and not l[m]:
            l[m] = v + 1
            q.append((m, v + 1))
