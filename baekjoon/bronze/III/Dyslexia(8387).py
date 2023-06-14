n = int(input())
a, b = input(), input()
x = 0
for i in range(n):
    x += a[i] != b[i]
print(x)
