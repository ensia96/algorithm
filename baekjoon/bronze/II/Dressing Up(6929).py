n = int(input())
x, y = '* '
A = [x*i+y*(n-i)+y*(n-i)+x*i for i in range(1, n+1, 2)]
for a in A+A[-2::-1]:
    print(a)
