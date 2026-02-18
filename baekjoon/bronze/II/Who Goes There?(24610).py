n, m, *T = map(int, open(i := 0).read().split())
R = [0] * m
while (n - sum(R)) * sum(T):
    x = T[i] > 0
    R[i] += x
    T[i] -= x
    i = -~i % m
print(*R, sep='\n')
