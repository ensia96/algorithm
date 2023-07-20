a, b, c = map(int, input().split())
print(b < c and a*b or (~-c+b//c)*a)
