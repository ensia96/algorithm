n = int(input())
L = [*map(int, input().split())]
H = [*map(int, input().split())]
D = [0]*100
for i in range(n):
    D = [max(D[j], (D[j-L[i]]+H[i])*(j >= L[i]))for j in range(100)]
print(max(D))
