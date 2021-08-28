import collections as c

n, k = map(int, input().split())
q, v = c.deque([(n, 0)]), 0

while 1:
    if c == k:
        print(v)
        break
    c, v = q.popleft()
    q.append((c * 2, v + 1))
    q.append((c - 1, v + 1))
    q.append((c + 1, v + 1))
