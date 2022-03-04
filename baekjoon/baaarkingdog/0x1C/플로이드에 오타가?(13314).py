print(100)
D = [[1-int(i == j or i == 99 or j == 99)for j in range(100)]
     for i in range(100)]
for _ in D:
    print(*_)
