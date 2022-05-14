n = int(input())
a = b = 1
for _ in ' '*n:
    a, b = b, a+b
print(b*2)
