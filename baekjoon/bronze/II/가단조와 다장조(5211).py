A = input()
l, A = A[-1], "".join(i[0] for i in A.split("|")).count
x, y = sum(map(A, "CFG")), sum(map(A, "ADE"))
print("CA--mmaijnoorr"[x < y + (x == y) * (l in "ADE") :: 2])
