input()
a = c = m = 0
for i in map(int, input().split()):
    if a < i:
        a, c = i, 0
    else:
        c += 1
    m = max(m, c)
print(m)
