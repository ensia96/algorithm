t = 0
for i, j in sorted((*map(int, input().split()),)for _ in ' '*int(input())):
    t = max(t, i)+j
print(t)
