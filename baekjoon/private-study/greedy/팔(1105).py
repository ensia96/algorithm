l, r = input().split()
x, y = len(l), 0
if x-len(r):
    print(y)
else:
    for i in range(x):
        if l[i] == r[i]:
            y += l[i] == '8'
        else:
            break
    print(y)
