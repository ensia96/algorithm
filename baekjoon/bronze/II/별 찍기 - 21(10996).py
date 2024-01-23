n = int(input())
t = ['*']
for _ in t*n:
    print(*t*-(n//-2))
    n > 1 and print(*(['']+t*(n//2)))
