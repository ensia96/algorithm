n, c = map(int, input().split())
n = n // 4
S = input()
for _ in c % 4 * ' ':
    S = S[:n] + S[-n:] + S[n:-n]
print(S)
