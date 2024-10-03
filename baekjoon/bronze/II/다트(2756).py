for l in [*open(0)][1:]:
    (*A,) = map(float, l.split())
    A = [
        int(max(6 + min(((i * i + j * j) / 9) ** 0.5 // -1, -1), 0) * 20)
        for i, j in zip(A[::2], A[1::2])
    ]
    x, y = sum(A[:3]), sum(A[3:])
    print(
        "SCORE:",
        f"{max(x,y)} to {min(x,y)},",
        [f"PLAYER {(x>y)+2*(x<y)} WINS.", "TIE."][x == y],
    )
