n = int(input())
d = [9, 17]
_ = [d.append((d[i-2]*2)+d[i-1]-((i-1)*i)) for i in range(2, n)]
print(d[n-1])
