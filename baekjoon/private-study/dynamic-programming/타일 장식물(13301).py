n = int(input())
a, b = 4, 6
for _ in ' '*~-n:
    a, b = b, a+b
print(a)
