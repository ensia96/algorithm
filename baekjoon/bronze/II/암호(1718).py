a, b = open(0)
y = ''
for i in range(len(a)-1):
    x = ord(a[i])-ord(b[i % ~-len(b)])
    y += [a[i], chr(96+x+26*(x < 1))][a[i].isalpha()]
print(y)
