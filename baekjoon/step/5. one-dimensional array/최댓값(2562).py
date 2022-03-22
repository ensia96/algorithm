a, b = 0, 0
for i in range(1, 10):
    x = int(input())
    if a < x:
        a, b = x, i
print(a)
print(b)
