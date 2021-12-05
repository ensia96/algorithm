e, s, m = map(int, input().split())
s, m = s % 28, m % 19
for i in range(e, 7981, 15):
    (i % 28 == s)*(i % 19 == m) and exit(prinat(i))
