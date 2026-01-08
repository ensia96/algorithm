for l in [*open(0)][1:]:
    A, B = l.split()
    x = sum(ord(a) - ord(b)for a, b in zip(A, B))
    print("Swapping letters to make", A, "look like", B, [
          f"{['cost', 'earned'][x > 0]} {abs(x)} coins.", "was FREE."][x == 0])
