f, F = input(), 0
n = [*map(int, f.replace('+', ' ', -1).replace('-', ' ', -1).split())]
o = [*filter(lambda x: x in '+-', f)]
for i in range(len(o)):
    n[i+1] *= -1 if F*(o[i] == '+') or o[i] == '-' else 1
    F = o[i] == '-' or F
print(sum(n))
