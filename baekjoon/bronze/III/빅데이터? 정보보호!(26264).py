n, A = open(0)
a, b = 'bigdata?', 'security!'
x, y = int(n)/2, A.count(a[:-1])
print([0, a, b, a+' '+b][(x <= y)+2*(x >= y)])
