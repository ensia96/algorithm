S = ''.join(filter(lambda x: x not in '01234565789', input()))
K = input()
f, j = [0]*len(K), 0
for i in range(1, len(K)):
    while j and K[i] != K[j]:
        j = f[j-1]
    if K[i] == K[j]:
        j += 1
        f[i] = j
j = 0
for i in range(len(S)):
    while j and S[i] != K[j]:
        j = f[j-1]
    j += S[i] == K[j]
    j-len(K) or exit(print(1))
print(0)
