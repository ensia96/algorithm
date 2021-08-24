import sys

n, s, a, c, f = int(input()), [], [], 1, 1

for _ in range(n):
    i = int(sys.stdin.readline().strip())
    while c <= i:
        s.append(c)
        a.append("+")
        c += 1
    if s[-1] == i:
        s.pop()
        a.append("-")
    else:
        f = 0

print("\n".join(a) if f else "NO")
