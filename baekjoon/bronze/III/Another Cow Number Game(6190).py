n = int(input())
x = 0
while n > 1:
    n = [n//2, n*3+1][n % 2]
    x += 1
print(x)
