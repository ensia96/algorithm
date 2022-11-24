input()
H = 2**20*[0]
for h in map(int, input().split()):
    if H[h+1]:
        H[h+1] -= 1
    H[h] += 1
print(sum(H))
