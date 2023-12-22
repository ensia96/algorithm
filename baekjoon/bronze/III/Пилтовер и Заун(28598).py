a, b, c = map(int, input().split())
x = a-b
print('YNEOS'[c and x/c <= 2 or x % 2::2])
