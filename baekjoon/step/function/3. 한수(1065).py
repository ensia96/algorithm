x, y = int(input()), 0


def check(num, gap):
    if num < 10:
        return 1
    if gap == (num % 10) - (num // 10 % 10):
        return check(num // 10, gap)
    return 0


for i in range(1, x + 1):
    y += check(i, (i % 10) - (i // 10 % 10))

print(y)
