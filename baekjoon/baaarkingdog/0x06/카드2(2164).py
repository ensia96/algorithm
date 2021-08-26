import collections as c

n, i = int(input()), 1
q = c.deque(i + 1 for i in range(n))

while q:
    if len(q) == 1:
        print(q.pop())
        break
    if i % 2:
        q.popleft()
    else:
        q.rotate(-1)
    i += 1
