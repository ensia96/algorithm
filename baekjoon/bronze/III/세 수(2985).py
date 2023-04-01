a, b, c = input().split()
for i in '+-*/':
    x, y = a+i+b+'=='+c, a+'=='+b+i+c
    z = eval(x)+2*eval(y)
    z and exit(print([y, x][-z].replace('==', '=')))
