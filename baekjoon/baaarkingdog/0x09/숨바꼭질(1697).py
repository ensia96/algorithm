import collections as c

n, k = map(int, input().split())
q, l = c.deque([n]), [0] * 100000

while q:
    c = q.popleft()
    if n == k or l[k]:
        print(l[k])
        break
    for m in [c - 1, c + 1, c * 2]:
        if 0 <= m < 100000 and not l[m]:
            l[m] = l[c] + 1
            q.append(m)
