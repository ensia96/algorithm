*L, _ = open(y := 0)
for l in L[1::2]:
    y += 1
    (*A,) = map(int, l.split())
    x = sum(A) // len(A)
    print(f"Set #{y}")
    print(f"The minimum number of moves is {sum(abs(a-x)for a in A)//2}.")
