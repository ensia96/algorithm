n = int(input())
R = range(n)
for i in R:
    print(*[i * n + j + 1 for j in R][::(-1)**(i % 2)])
