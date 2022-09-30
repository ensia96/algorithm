A = input()
D = [0]*26
R, r = '', ''
for a in A:
    x = ord(a)-ord('A')
    D[x] += 1
if sum(d % 2 for d in D) > 1:
    R = "I'm Sorry Hansoo"
else:
    for i in range(26):
        t = chr(i+ord('A'))
        if D[i] % 2:
            r = t
        R += D[i]//2*t
    R = R+r+R[::-1]
print(R)
