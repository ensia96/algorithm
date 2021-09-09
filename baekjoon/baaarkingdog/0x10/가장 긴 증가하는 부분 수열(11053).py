n = int(input())
a = [*map(int, input().split())]
d = [(a[0], 1)]
_ = [d.append((max(d[i-1][0], a[i]), d[i-1][1]+(d[i-1][0] < a[i])))
     for i in range(1, n)]
print(d[-1][1])
