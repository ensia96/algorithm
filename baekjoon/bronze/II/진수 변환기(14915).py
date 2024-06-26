a, b = map(int, input().split())
s = ''
while a:
    a, r = divmod(a, b)
    s = '0123456789ABCDEF'[r]+s
print(s or 0)
