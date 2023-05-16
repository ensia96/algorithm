a, b, c = map(int, input().split())
x, y, z = (b-c+a)/2, (a-b+c)/2, (c-a+b)/2
A = x > 0 and y > 0 and z > 0
print(-1+2*A)
A and print(x, y, z)
