n = int(input())
print(sum(b*b+n == a*a for b in range(501)for a in range(b, 501)))
