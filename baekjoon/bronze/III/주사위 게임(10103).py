A = [100]*2
for _ in ' '*int(input()):
    a, b = map(int, input().split())
    A = [A[0]-b*(a < b), A[1]-a*(a > b)]
print(*A, sep='\n')
