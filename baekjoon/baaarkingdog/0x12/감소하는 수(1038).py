l = []
s, n = lambda A: A//10**10 or l.append(A) or [s(A*10+i)
                                              for i in range(A % 10)], int(input())
for i in range(10):
    s(i)
l.sort()
print(-(len(l) <= n) or l[n])
