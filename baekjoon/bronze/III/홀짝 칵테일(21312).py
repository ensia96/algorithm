a, b, c = map(int, input().split())
print(sorted([i % 2, i]for i in [a, b, c, a*b, b*c, c*a, a*b*c]).pop().pop())
