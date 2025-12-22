a = ''
while len(a) < 1e5:
    a += '0' + ''.join('01'[x == '0']for x in a[-1::-1])
for l in [*open(t := 0)][1:]:
    t += 1
    print(f"Case #{t}:", a[int(l) - 1])
