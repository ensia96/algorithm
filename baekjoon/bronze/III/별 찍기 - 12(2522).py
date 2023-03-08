n = int(input())
print('\n'.join([' '*abs(i)+'*'*(n-abs(i))for i in range(1-n, n)]))
