a, _ = 0, input()

for n in map(int, input().split()):
    x = 0
    for i in range(1, n):
        if n % i == 0:
            x += 1
    if x == 1:
        a += 1

print(a)
