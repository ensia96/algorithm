A = [*open(0)][1:]
a = ''
for i in range(26):
    t = chr(i+97)
    if sum(t == a[0]for a in A) > 4:
        a += t
print(a or 'PREDAJA')
