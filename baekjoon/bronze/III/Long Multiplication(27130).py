A, B = open(0).read().split()
y = 0
print(A)
print(B)
for b in B[::-1]:
    x = eval(b+'*'+A)
    print(x)
    y += x
print(eval(A+'*'+B))
