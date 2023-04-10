n = int(input())
x = i = 0
while x < n:
    x, i = sum((i+1)**j for j in range(3)), i+1
print(i)
