A = "".join(i[0] for i in input().split("|"))
A = (A + A[-1]).count
print("CA--mmaijnoorr"[sum(map(A, "ADE")) > sum(map(A, "CFG")) :: 2])
