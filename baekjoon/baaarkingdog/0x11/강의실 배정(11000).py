import sys
i, l, m = sys.stdin.readline, [0], 0
for s, e in sorted((*map(int, i().split()),)for _ in ' '*int(i())):
    for j in range(len(l)):
        if l[j] <= s:
            l[j] = e
            break
    else:
        l += [e]
print(len(l))
