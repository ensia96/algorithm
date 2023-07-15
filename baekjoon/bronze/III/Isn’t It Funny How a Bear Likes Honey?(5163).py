import math
A = []
for i in range(int(input())):
    a, b = input().split()
    A += f"Data Set {i+1}:\n{'YNeos'[float(b)>sum(4/3000*math.pi*float(input())**3 for _ in' '*int(a))::2]}",
print('\n\n'.join(A))
