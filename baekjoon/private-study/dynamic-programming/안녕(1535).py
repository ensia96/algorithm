n = int(input())
L = [*map(int, input().split())]
H = [*map(int, input().split())]
D = [0]*100
for i in range(n):
    D = [0]+[max((H[i]+D[j-L[i]])*(L[i] < j), D[j])for j in range(1, 100)]
print(D[-1])
