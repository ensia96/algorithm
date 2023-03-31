c, k, p = map(int, input().split())
print(sum(-~i*(k+-~i*p)for i in range(c)))
