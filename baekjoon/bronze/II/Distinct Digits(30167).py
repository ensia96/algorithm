l, r = map(int, input().split())
t = -1
for i in range(l, r+1):
    if len(s := str(i)) == len({*s}):
        t = i
        break
print(t)
