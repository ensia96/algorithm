D = [1]+[0]*35
for i in range(35):
    for j in range(i+1):
        D[i+1] += D[i-j]*D[j]
print(D[int(input())])
