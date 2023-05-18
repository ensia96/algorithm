n = int(input())/2
f = [*map(int, input().split())].count
print(['INVALID', ['APPROVED', 'REJECTED'][f(1) < n]][f(0) < n])
