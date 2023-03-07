n = int(input())
print('\n'.join([i*'*'for i in [*range(1, n), *range(n, 0, -1)]]))
