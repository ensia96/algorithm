n = int(input())
n < 2 and exit(print("*"))
N = range(n)
for i in N:
    print(
        "".join(
            " *"[not (i % ~-n) or i == j or not (j % ~-n) or i + j == ~-n] for j in N
        )
    )
