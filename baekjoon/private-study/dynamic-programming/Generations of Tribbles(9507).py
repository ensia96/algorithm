D = [1, 1, 2, 4]
for i in range(4, 68):
    D += D[i-1]+D[i-2]+D[i-3]+D[i-4],
for _ in ' '*int(input()):
    print(D[int(input())])
