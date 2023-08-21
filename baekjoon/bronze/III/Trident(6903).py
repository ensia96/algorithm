a, b, c = map(int, open(0).read().split())
x, y = '* '
exec('print(x+y*b+x+y*b+x);'*a)
print(x*(b+b+3))
exec('print(y*-~b+x);'*c)
