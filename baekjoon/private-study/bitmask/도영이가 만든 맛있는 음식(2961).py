n = int(input())
A = [(1, 0)]
for _ in ' '*n:
    s, b = map(int, input().split())
    A += [(x*s, b-y)for x, y in A]
print(min(abs(x-y)for x, y in A))
