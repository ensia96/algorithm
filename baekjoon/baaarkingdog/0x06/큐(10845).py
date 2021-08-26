import collections as c

p, i = print, input
n, q = int(i()), c.deque()

for _ in range(n):
    c = i()
    if c == "pop":
        p(q.popleft() if q else -1)
    elif c == "size":
        p(len(q))
    elif c == "empty":
        p(int(not bool(q)))
    elif c == "front":
        p(q[0] if q else -1)
    elif c == "back":
        p(q[-1] if q else -1)
    else:
        q.append(c.split().pop())
