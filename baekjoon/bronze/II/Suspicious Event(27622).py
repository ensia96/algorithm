input()
D = {}
c = 0
for i in map(int, input().split()):
    if i > 0:
        D[i] = 1
    elif -i not in D:
        c += 1
print(c)
