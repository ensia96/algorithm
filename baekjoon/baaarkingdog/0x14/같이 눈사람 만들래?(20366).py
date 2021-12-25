n, D = int(input()), 4*10**9
H = sorted(map(int, input().split()))
for a in range(n-3):
    for d in range(a+3, n):
        A, b, c = H[a]+H[d], a+1, d-1
        while b < c:
            B = H[b]+H[c]
            D = min(D, abs(A-B))
            if A == B:
                exit(print(0))
            b, c = b+(A > B), c-(A < B)
print(D)
