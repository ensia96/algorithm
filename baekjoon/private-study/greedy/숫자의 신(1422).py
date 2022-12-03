k, n = map(int, input().split())
A = sorted([input()for _ in ' '*k], key=lambda x: (len(x), x*10))
A += A[-1]*(n-k),
print(''.join(sorted(A, key=lambda x: x*10)[::-1]))
