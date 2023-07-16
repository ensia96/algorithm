a, b, c = map(int, input().split())
print(sum(str(i).count(str(c))for i in range(a, b+1)))
