A = input()
x = {*'1234'} - {*A}
print(*[[A[:3]], [A.find('0') // 2 + 1, *x], sorted(x)][len(x)])
