m = [0] * 10001
for _ in range(int(input())):
    m[int(input())] += 1
print()
for i in range(10001):
    for j in range(m[i]):
        print(i)
