m, n = map(int, input().split())

for i in range(m, n + 1):
    if all(i % j for j in range(2, i)):
        print(i)
