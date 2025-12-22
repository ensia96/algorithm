a = '0'
while len(a) < 1e5:
    a += '0' + ''.join('01'[x == '0']for x in a[-2::-1])
for l in [*open(t := 0)][1:]:
    t += 1
    print(f"Case #{t}:", a[int(l)])
