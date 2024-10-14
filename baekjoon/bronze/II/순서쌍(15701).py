n = int(input())
print(sum((2 - (i * i == n)) * (n % i == 0) for i in range(1, int(n**0.5) + 1)))
