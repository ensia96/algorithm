import sys

i, b = sys.stdin.readline, {'(': ')', '[': ']'}
o, c = b.keys(), b.values()

while 1:
    t = i().rstrip()
    a, s = 'yes', []
    if t == '.':
        break

    for l in t:
        if l in o:
            s.append(l)
        if l in c:
            if not s or l != b[s[-1]]:
                a = 'no'
                break
            s.pop()
    print(a)
