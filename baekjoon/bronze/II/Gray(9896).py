input()
n = input()
print(n[0], *['10'[a == b]for a, b in zip(n, n[1:])], sep='')
