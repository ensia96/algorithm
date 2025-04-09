A = input().split("+")
print(
    ["No Money", "CUTE"][
        2 == len(A) and A[0] == A[1] and A[0].isdigit() and A[0][0] != "0"
    ]
)
