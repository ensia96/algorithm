n = int(input())
l = [*map(int, input().split())]
d = [l[0]]
_ = [d.append(max(d[i-1]+l[i], l[i])) for i in range(1, n)]
print(max(d))
