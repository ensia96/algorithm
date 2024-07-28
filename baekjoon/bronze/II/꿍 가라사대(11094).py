for l in [*open(0)][1:]:
    _, *A = l.strip().split("Simon says")
    A and print(*A)
