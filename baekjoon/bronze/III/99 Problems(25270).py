a = input()
n, l = int(a), len(a)-1
M = int(a[0]+'9'*l)
m = M-10**l
print(max(99, [M, m][abs(n-m) < abs(n-M)]))
