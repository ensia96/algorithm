s = input()
p = input()
f, j = [0]*len(p), 0
for i in range(1, len(p)):
    while j > 0 and p[i] != p[j]:
        j = f[j-1]
    if p[i] == p[j]:
        j += 1
        f[i] = j
j = 0
for i in range(len(s)):
    while j > 0 and s[i] != p[j]:
        j = f[j-1]
    j += s[i] == p[j]
    j-len(p) or exit(print(1))
print(0)
