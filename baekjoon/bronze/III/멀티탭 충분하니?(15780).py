n, k = map(int, input().split())
print('YNEOS'[n > sum(sum(divmod(i, 2))for i in map(int, input().split()))::2])
