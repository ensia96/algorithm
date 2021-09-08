p, l = 2, [0, 0]
for i in map(int, input()):
    if i != p:
        l[i], p = l[i]+1, i
print(min(l))
