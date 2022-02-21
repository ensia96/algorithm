A = 0
for _ in ' '*int(input()):
    w, t = [*input()], []
    while w:
        if t and t[-1] == w[-1]:
            t.pop()
            w.pop()
        else:
            t += w.pop(),
    A += not t
print(A)
