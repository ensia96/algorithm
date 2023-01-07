n = int(input())
print(sum(divmod(n, 10 if n % 10 else 100)))
