def stringsRearrangement(inputArray):
    import difflib

    for i, j in [(i, j) for i in inputArray for j in inputArray if i != j]:
        print([s for s in list(difflib.ndiff(i, j)) if s[0] != " "])


# print(stringsRearrangement(["ab", "bb", "aa"]))
# => should return True

print(stringsRearrangement(["aba", "bbb", "bab"]))
# => should return False
