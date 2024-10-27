j, *A = open(0)
print(
    sum(
        int(j[0])
        >= sum(
            i.isupper() * 4 + (i.islower() + i.isdigit()) * 2 + (i == " ") for i in a
        )
        for a in A
    )
)
