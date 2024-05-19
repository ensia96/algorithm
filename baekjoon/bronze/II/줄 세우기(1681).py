n, l = input().split()
n, x = int(n), 0
while n:
    x += 1
    n -= l not in str(x)
print(x)
