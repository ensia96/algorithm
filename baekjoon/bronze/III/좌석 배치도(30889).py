D = [20*['.']for _ in ' '*10]
for a in open(0).read().split()[1:]:
    D[ord(a[0])-65][int(a[1:])-1] = 'o'
for d in D:
    print(''.join(d))
