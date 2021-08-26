import collections as c

n, i = int(input()), 1
q = c.deque(range(1, n + 1))

while q:
    if len(q) == 1:
        print(q.pop())
    if i % 2:
        q.popleft()
    else:
        q.rotate(-1)
    i += 1
