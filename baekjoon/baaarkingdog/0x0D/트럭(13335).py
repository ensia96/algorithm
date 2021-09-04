import collections as c
d, t = lambda: map(int, input().split()), 0
n, w, l = d()
k, b = [*d()][::-1], c.deque([0]*w)

while k:
    b[0] = 0
    b.rotate(-1)
    t += 1
    if sum(b) + k[-1] <= l:
        b.pop()
        b.append(k.pop())

print(t+len(b))
