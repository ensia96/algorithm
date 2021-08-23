a, b = sorted(map(int, input().split()))
l = [i for i in range(a + 1, b)]
print(len(l))
print(*l)
