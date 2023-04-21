n = int(input())
x = y = i = 2
j = 0
while i < n and x > 0:
    j += x*(not y)
    x, y = divmod(n-2*i, 2)
    i += 2
print(j)
