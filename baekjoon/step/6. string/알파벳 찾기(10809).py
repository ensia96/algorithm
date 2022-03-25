a = {_: -1 for _ in "abcdefghijklmnopqrstuvwxyz"}

for i, s in enumerate(input()):
    if a[s] == -1:
        a[s] = i

print(*a.values())
