from itertools import combinations as t
i, m = input, 'aeiou'
l, c = map(int, i().split())
s = i().split()
m, s = [*filter(lambda x: x in m, s)], [*filter(lambda x: x not in m, s)]

print('\n'.join(sorted(
    [''.join(sorted(''.join(x) + ''.join(y)))
     for i in range(2, l) for x in [*t(m, l-i)] for y in [*t(s, i)]])))
