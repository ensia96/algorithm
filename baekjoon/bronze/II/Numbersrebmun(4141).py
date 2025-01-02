D = {"abc": 2, "def": 3, "ghi": 4, "jkl": 5, "mno": 6, "pqrs": 7, "tuv": 8, "wxyz": 9}
for l in [*open(0)][1:]:
    print(
        "YNEOS"[
            1
            ^ all(
                any((a in d) and (b in d) for d in D)
                for a, b in zip(l.lower()[-2::-1], l.lower()[:-1:])
            ) :: 2
        ]
    )
