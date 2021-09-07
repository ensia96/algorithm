n = int(input())
c = [[*map(int, input().split())] for _ in range(n)]
d = [c[0]]
_ = [d.append((min(d[i-1][1:3])+c[i][0], min(d[i-1][::2])+c[i][1],
              min(d[i-1][:2])+c[i][2])) for i in range(1, n)]
print(min(d[-1]))
