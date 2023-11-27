n, *A, t, p = map(int, open(0).read().split())
print(sum(int(a/t+.9)for a in A))
print(*divmod(n, p))
