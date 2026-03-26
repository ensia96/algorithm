f = lambda: map(int, input().split())
n, H = f()
W = 0
exec("s=sorted(f());s[0]>H>exit(print('impossible'));W+=s[s[1]>H];" * n)
print(W)
