j, n = map(int, input().split())
print(
    sum(
        j
        >= sum(
            i.isupper() * 4 + (i.islower() + i.isdigit()) * 2 + (i == " ")
            for i in input()
        )
        for _ in " " * n
    )
)
