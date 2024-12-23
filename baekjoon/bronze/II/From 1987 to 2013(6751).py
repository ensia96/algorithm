n = input()
while len(n := str(int(n) + 1)) > len({*n}):
    n
print(n)
