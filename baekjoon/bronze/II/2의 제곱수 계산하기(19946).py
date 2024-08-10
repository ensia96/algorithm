n = int(input())
i = 64
while n % 2 < 1:
    n //= 2
    i -= 1
print(i)
