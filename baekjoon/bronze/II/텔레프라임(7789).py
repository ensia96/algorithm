n, m = input().split()
n, m = int(n), int(m + n)
i = 2
while i * i <= m:
    (not m % i or i * i <= n and not n % i) and exit(print("No"))
    i += 1
print("Yes")
