n = int(input())/2
f = [*map(int, input().split())].count
print(['INVALID', ['REJECTED', 'APPROVED'][f(1) > f(-1)]][f(0) < n])
