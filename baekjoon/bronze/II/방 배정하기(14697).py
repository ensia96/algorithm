a, b, c, n = map(int, input().split())
print(+(n % c % b % a < 1))
