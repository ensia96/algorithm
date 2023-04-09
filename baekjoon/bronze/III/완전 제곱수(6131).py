n = int(input())
A = {-~i**2 for i in range(500)}
print(sum(-~i**2-n in A for i in range(500)))
