n = int(input())
A = input()
m = len(A)-1
S = [0]*26
x = l = r = 0
c = S[ord(A[0])-97] = 1
m or exit(print(+bool(n)))
while r < m:
    if c <= n:
        r += 1
        y = ord(A[r])-97
        c += not S[y]
        S[y] += 1
    else:
        y = ord(A[l])-97
        S[y] -= 1
        c -= not S[y]
        l += 1
    x = max(x, (r-l+1)*(c <= n))
print(x)
