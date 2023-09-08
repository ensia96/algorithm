x = '*'
n = int(input())
for i in range(1, n+1):
    print(x*100+'...'if i > 10 else x*i*i)
