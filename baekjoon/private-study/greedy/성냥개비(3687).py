d = [0, 0, 1, 7, 4, 2, 0, 8, 10]
D = [0, 0, 1, 7, 4, 2, 6, 8, 10]
for i in range(9, 101):
    D += min(D[i-j]*10+d[j]for j in range(2, 8)),
for _ in ' '*int(input()):
    n = int(input())
    print(D[n], '17'[n % 2]+~-n//2*'1')
