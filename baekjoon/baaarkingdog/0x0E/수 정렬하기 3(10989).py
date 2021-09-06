import sys
i, g = sys.stdin.readline, range
m = [0] * 10001
for _ in g(int(i())):
    m[int(i())] += 1
for a in g(10001):
    for _ in g(m[a]):
        print(a)
