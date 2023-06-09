n = int(input())
print(sum(i+j == n for i in range(6)for j in range(i, 6)))
