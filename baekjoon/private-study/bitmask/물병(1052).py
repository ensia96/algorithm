n, k = map(int, input().split())
a = 0
while 1:
    bin(n+a).count('1') <= k and exit(print(a))
    a += 1
