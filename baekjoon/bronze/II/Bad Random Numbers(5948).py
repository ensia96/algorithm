n = input().zfill(4)
N = [n]
while 1:
    n = str(int(n[1:3]) ** 2).zfill(4)
    if n in N:
        break
    N += (n,)
print(len(N))
