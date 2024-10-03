for l in [*open(0)][1:]:
    (*A,) = map(float, l.split())
    A = [
        20 * sum((-~k) ** 2 * 9 >= (i * i + j * j) for k in range(5))
        for i, j in zip(A[::2], A[1::2])
    ]
    x, y = sum(A[:3]), sum(A[3:])
    print(
        "SCORE:",
        f"{max(x,y)} to {min(x,y)},",
        [f"PLAYER {(x>y)+2*(x<y)} WINS.", "TIE."][x == y],
    )
