s, _, *A = open(0).read().split()
for a in A:
    print(*map(sum, zip(*[(a[i] in s, a[i] == s[i])for i in range(4)])))
