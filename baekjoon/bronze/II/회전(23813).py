n = input()
S = 0
for i in range(len(n)):
    n = n[-1] + n[:-1]
    S += int(n)
print(S)
