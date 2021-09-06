import sys
_, *n = input().split()
for l in sys.stdin:
    n += l.split()
print(*sorted(map(int, [i[::-1] for i in n])))
