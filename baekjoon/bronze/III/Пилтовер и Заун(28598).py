a, b, c = map(int, input().split())
x = a-b
print('YNEOS'[x % 2 or c and x/c <= 1::2])
