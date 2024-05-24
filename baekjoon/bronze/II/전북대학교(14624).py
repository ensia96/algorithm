n, x, y = int(input()), *'* '
n % 2 or exit(print('I LOVE CBNU'))
A = [x*n, n//2*y+x]+[(n//2-i-1)*y+x+y*(2*i+1)+x for i in range(n//2)]
for a in A:
    print(a)
