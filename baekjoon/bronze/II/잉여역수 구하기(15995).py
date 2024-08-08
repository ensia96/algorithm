a, m = map(int, input().split())
for i in range(1, 10001):
    a * i % m == 1 and exit(print(i))
