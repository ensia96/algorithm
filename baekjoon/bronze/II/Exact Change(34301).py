n = int(input())
print(*[n // i * ((n := n % i) - n + 1)for i in [150, 30, 15, 5, 1]][::-1])
