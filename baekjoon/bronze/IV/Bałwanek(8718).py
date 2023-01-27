x, k = map(int, input().split())
print(k*(7000 if k*7 <= x else 3500 if k*3.5 <= x else 1750 if k*1.75 <= x else 0))
