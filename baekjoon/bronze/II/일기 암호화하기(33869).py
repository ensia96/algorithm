w, s = input(), input()
D = []
for i in w:
    if i not in D:
        D += i,
D += [x for i in range(26)if (x := chr(65+i))not in D]
print(''.join(D[ord(i)-65]for i in s))
