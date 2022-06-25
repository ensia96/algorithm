x = int(input())
print(sum(bool(x & 1 << i)for i in range(7)))
