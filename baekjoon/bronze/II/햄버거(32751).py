_, A, B = open(0)
(*A,) = map(int, A.split())
print(
    "YNeos"[
        (
            B[0] == B[-2] == "a"
            and all(a != b for a, b in zip(B, B[1:]))
            and all(B.count(b) <= A[ord(b) - 97] for b in B[:-1])
        )
        ^ 1 :: 2
    ]
)
