a, b, *A = map(int, open(0).read().split())
print(sum(a**b*((a > 0)+(a < 0)*(b % 2 == 0))for a in A))
