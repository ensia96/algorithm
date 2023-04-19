i = 1
for l in [*open(0)][:-1]:
    a, b, c = map(int, l.split())
    print(f'Triangle #{i}')
    A, B, C = c*c-b*b, c*c-a*a, a*a+b*b
    a < 0 and print(['Impossible.', f'a = {A**.5:.3f}'][A > 0])
    b < 0 and print(['Impossible.', f'b = {B**.5:.3f}'][B > 0])
    c < 0 and print(['Impossible.', f'c = {C**.5:.3f}'][C > 0])
    i += 1
    print()
