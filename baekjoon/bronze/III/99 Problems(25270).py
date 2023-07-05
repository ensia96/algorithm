n = int(input())
for i in range(100):
    (n+i) % 100 == 99 and exit(print(n+i))
    (n-i) % 100 == 99 and exit(print(max(n-i, 99)))
