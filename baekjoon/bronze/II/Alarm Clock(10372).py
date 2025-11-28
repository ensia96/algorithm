L = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
R = range(10)
n = int(input())
for i in R:
    for j in R:
        for k in R:
            for l in R:
                if L[i] + L[j] + L[k] + L[l] == n and 10 * i + j < 24 and 10 * k + l < 60:
                    exit(print(f"{i}{j}:{k}{l}"))
print("Impossible")
