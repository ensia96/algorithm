import sys
p, l = 2, [0, 0]
for i in map(int, sys.stdin.readline()):
    if i != p:
        l[i], p = l[i]+1, i
print(min(l))
