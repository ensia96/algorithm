A = 0
for _ in ' '*int(input()):
    t = []
    for i in input():
        t and t[-1] == i and t.pop() or t.append(i)
    A += not t
print(A)
