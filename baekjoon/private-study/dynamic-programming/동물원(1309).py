n, m = int(input()), 9901
a = b = c = 1
for i in ' '*~-n:
    a, b, c = (a+b+c) % m, (a+c) % m, (a+b) % m
print(a+b+c)
