n, m = map(int, input().split())
print('YNEOS'[n*m % 3 > 0::2])
