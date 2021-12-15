L, T = lambda: map(int, input().split()), []
M, N = L()
S = [[*L()]for _ in range(M)]
for i in range(M):
    s = S[i]
    c, t = [*sorted(set(s))], []
    for j in range(N):
        l, r, k = 0, N, s[j]
        while l < r:
            m = (l+r)//2
            if c[m] < k:
                l = m
            elif c[m] > k:
                r = m
            else:
                t += [m]
                break
    S[i] = (*t,)
print(sum(S[i] == S[j]for i in range(M)for j in range(i+1, M)))
