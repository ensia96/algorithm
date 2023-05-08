A = []
for i in range(int(input())):
    s, c, l = map(int, input().split())
    A += [s, -c, -l, i+1],
print(sorted(A)[-1][-1])
