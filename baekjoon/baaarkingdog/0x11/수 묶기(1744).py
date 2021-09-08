I, R = input, range
l, a = lambda l: sum(l[i]*(not i or l[i-1]) for i in R(len(l)-1, -1, -2)), 0
u, d = [], []
for _ in R(int(I())):
    i = int(I())
    u, d, a = u+[[], [i]][i > 1], d+[[], [i]][i < 1], a+(i == 1)
print(a+l(sorted(u))+l(sorted(d)[::-1]))
