_, *L = open(0)
for i in range(int(_)):
    _, a = L[2*i].split()
    T = L[2*i+1].split()
    print(*[ord(t)-64 if a == 'C'else chr(int(t)+64)for t in T])
