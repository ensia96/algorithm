input()
A = "".join(sorted({*input()}))
print(
    ["NO!", "yes", "YES", "YeS"][
        all(i in A for i in "bgiorvy") + 2 * all(i in A for i in "BGIORVY")
    ]
)
