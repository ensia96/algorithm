n = int(input())
if n < 6:
    print(n)
else:
    x, y = divmod(n-5, 4)
    if x % 2:
        print(y+(x % 2))
    else:
        print(5-y)
