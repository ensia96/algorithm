a, b, c = map(int, input().split())
print(min(j for x in [a + b, a - b, a * b, a / b]if x % 1 ==
      0 for j in [x + c, x - c, x * c, x / c]if j % 1 == 0 and j >= 0))
