n, r = int(input()), 0

for i in range(n):
    if i + sum(map(int, list(str(i)))) == n:
        r = i
        break

print(r)
