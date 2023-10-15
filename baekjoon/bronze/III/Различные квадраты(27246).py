n = int(input())
i = 1
while n >= i*i:
    n -= i*i
    i += 1
print(i-1)
