input()
A = "".join(sorted(input()))
print(["NO!", "yes", "YES", "YeS"][("bgiorvy" in A) + 2 * ("BGIORVY" in A)])
