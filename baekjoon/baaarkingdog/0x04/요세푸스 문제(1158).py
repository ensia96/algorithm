import collections as c

n, k = map(int, input().split())
l, a = c.deque([str(i + 1) for i in range(n)]), []

while l:
    l.rotate(-k)
    a.append(l.pop())

print(f"<{', '.join(a)}>")
