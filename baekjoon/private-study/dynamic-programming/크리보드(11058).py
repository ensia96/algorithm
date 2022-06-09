D = [0]
for i in range(int(input())):
    D += max([j*D[i-j]for j in range(2, i)]+[D[i]+1]),
print(D[-1])
