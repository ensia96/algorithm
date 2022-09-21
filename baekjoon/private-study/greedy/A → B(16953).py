a, b = map(int, input().split())
c = 1
while a < b:
    if not b % 2:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    c += 1
print(-1 if a-b else c)
