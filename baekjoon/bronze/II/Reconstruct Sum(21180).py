n, *A = map(int, open(0))
t = [a for a in A if sum(A)-a == a]
print(t[0]if len(t)else 'BAD')
