import sys

i, b = sys.stdin.readline, {'(': ')', '[': ']'}
o, c = b.keys(), b.values()

while 1:
    t, f, s = i().rstrip(), 1, []

    if t == '.':
        break

    for l in t:
        if l in o:
            s.append(l)
        if l in c:
            if not s or l != b[s[-1]]:
                f = 0
                break
            s.pop()
    print('no' if not f or s else 'yes')
