a, b = input().split()
T = {eval(t := a+i+[b, f'({b})']['-' in b]): t for i in '+-*'}
print(T[m := max(T)]+'='+str(m))
