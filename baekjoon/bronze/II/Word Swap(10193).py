for l in [*open(0)][1:]:
    A, B = l.split()
    x = sum(ord(a) - ord(b)for a, b in zip(A, B))
    print("Swapping letters to make", A, "look like",
          B, ["was FREE.", f"earned {x} coins."][x > 0])
