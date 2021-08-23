n = int(input())

for i in [*range(n - 1, 0, -1)] + [*range(n)]:
    print("*" * (n - i) + " " * (2 * i) + "*" * (n - i))
