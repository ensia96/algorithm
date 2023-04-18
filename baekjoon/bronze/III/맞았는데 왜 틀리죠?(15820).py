x, y = map(int, input().split())
a = x == sum(eval(input().replace(' ', '=='))for _ in ' '*x)
b = y == sum(eval(input().replace(' ', '=='))for _ in ' '*y)
print([['Wrong Answer', 'Why Wrong!!!'][a], 'Accepted'][a*b])
