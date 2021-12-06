l = []
s, n = lambda a, b: l.append(b) or [s(i, b*10+i)
                                    for i in range(a)], int(input())
s(10, 0)
l.sort()
print(-(len(l)-2 < n) or l[n+1])
