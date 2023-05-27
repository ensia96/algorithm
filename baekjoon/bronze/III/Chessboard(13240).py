n, m = map(int, input().split())
x = '*.'*11
for i in range(n):
    print(x[i % 2:m+i % 2])
