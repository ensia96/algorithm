n = int(input())
A = {i*i for i in range(1, 501)}
print(sum(a+n in A for a in A))
