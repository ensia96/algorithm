a, b = input(), input()
i = max(map(len, [a, b]))
a, b = map(int, a.rjust(i, '0')), map(int, b.rjust(i, '0'))
print("".join('90'[i]for i in [i < 3 and j <
      3 or i > 6 and j > 6 for i, j in zip(a, b)]))
