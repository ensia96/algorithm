n = int(input())
print([0, int(n > 0 or n % 2 or -1)][bool(n)])
a, b = 0, 1
for i in ' '*abs(n):
    a, b = b % 10**9, a+b
print(a)
