n = int(input())
s, a = [(10e8, 0)], 0

for i in range(n):
    h = int(input())
    while s[-1][0] < h:
        v = s.pop()[1]
        a += i - v - 1
    s += [(h, i)]

while len(s) > 1:
    v = s.pop()[1]
    a += i - v

print(a)
