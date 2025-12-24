n, *A, _ = open(0)
S = [int(n)]
for a, b, _ in A:
    S += (S[-1] + int(b) * (1 - 2 * ('C' > a))) % 8 or 8,
print(*S + ['reject'] * (len(S) > len({*S}) or len({*S}) < 5))
