a, b, c = map(int, input().split())
x = a-b
if c == 0:
    print('YNEOS'[a != b::2])
elif x % 2 or x//2/c < 1:
    print('NO')
else:
    print('YES')
