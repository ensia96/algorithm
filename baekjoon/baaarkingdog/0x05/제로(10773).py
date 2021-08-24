import sys

s = []

for _ in range(int(input())):
    n = int(sys.stdin.readline().strip())
    if n:
        s.append(n)
    else:
        if s:
            s.pop()

print(sum(s))
