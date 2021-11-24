m, a = 2e5, 0
for s in [int(input())for _ in ' '*int(input())][::-1]:
    m = min(m-1, s)
    a += s-m
print(a)
