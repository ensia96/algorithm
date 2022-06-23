M = 1000000007
n = int(input())
n < 2 and exit(print(n))
a, b = 0, 1
for _ in ' '*n:
    a, b = b % M, (a+b) % M
print(a)
