n = int(input())
for i in range(1, n+1):
    x, y = i % 3 < 1, i % 5 < 1
    print(x*'Dead'+y*'Man'if x+y else i, end=[' \n'[x+y > 0], ''][i == n])
