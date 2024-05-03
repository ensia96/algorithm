n = int(input())//3
R = range(1, n+1)
print(sum(i+j < n for i in R for j in R))
