n = int(input())
for i in range(n):
    print(' '*(i % 2)+' '.join('*'*n))
