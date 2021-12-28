S = input()
n = len(S)
print(len({S[i:j+1]for i in range(n)for j in range(i, n)}))
