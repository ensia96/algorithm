n = int(input())
o, p = 1, 0
while 2**p < n:
    x, y = divmod(n, 2**p)
    if not y and x % 2:
        o = x
        break
    p += 1
print(o, p)
