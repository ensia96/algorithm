import sys

n, s, a, f = int(input()), [1], ["+"], 1
l = [*range(2, n + 1)[::-1]]

for _ in range(n):
    i = int(sys.stdin.readline().strip())
    if not s or s[-1] > i:
        f = 0
        continue
    while s[-1] < i:
        s.append(l.pop())
        a.append("+")
    if s[-1] == i:
        s.pop()
        a.append("-")

print("\n".join(a) if f else "NO")
