s = ''
for a in input():
    s += a
    if s[-4:] == 'PPAP':
        s = s[:-3]
print('NP'if'A' in s else'PPAP')
