a, b, c, d = int(input()), int(input()), int(input()), int(input())
print('Fish Rising'if a < b < c < d else 'Fish Diving'if a > b >
      c > d else 'Constant Depth'if a == b == c == d else 'No Fish')
