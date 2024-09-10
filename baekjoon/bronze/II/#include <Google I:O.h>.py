for i in range(int(input())):
    n = int(input())
    A = input()
    print(
        f"Case #{-~i}:",
        "".join(
            chr(int(A[i * 8 : -~i * 8].translate(str.maketrans("IO", "10")), 2))
            for i in range(n)
        ),
    )
