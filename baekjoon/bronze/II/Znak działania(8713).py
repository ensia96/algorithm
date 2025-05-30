a, b, f = *map(int, input().split()), lambda x: [f"{x}", f'({x})'][x < 0]
T = {eval(t := f(a)+i+f(b)): t for i in '+-*'}
print(T[m := max(T)]+'='+f(m))
