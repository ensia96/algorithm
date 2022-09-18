n = int(input())
i = 1
while n > 0:
    n -= i
    i += 1
print(0 if i % 2 else -n)
