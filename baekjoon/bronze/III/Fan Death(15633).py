n = int(input())
print(sum(-~i*(n % -~i < 1)for i in range(n))*5-24)
