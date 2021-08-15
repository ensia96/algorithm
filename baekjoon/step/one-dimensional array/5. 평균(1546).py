x, y = int(input()), list(map(int, input().split()))
a = max(y)
print(sum([i / a * 100 for i in y]) / x)
