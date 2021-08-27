import sys

a, s = 0, []

for i in sys.stdin.readline().strip().replace('()', '1'):
    if i == '(':
        s.append(i)
    elif i == ')':
        s.pop()
        a += 1
    else:
        a += len(s)

print(a)
