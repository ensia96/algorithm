n, m = map(int, input().split())
a = n
while n:
    n, _ = divmod(n, m)
    a += n
print(a)
