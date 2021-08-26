import sys as s, collections as c

p, i = print, s.stdin.readline
n, q = int(i().strip()), c.deque()

for _ in range(n):
    c = i().strip()
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
