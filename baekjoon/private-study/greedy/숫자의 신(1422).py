k, n = map(int, input().split())
A = [input()for _ in ' '*k]
print(*sorted(A+[max(A, key=int)]*(n-k), key=lambda x: x*10)[::-1]), sep='')
