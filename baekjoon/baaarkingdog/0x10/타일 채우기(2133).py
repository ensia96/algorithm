D = [1, 0, 3]
P = [0, 1, 0]
for i in range(3, int(input())+1):
    D, P = D+[D[i-2]+2*P[i-1]], P+[D[i-1]+P[i-2]]
print(D[-1])
