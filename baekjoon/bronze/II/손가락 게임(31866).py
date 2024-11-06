a, b = input().split()
if a in "025" and b not in "025":
    print(">")
elif a not in "025" and b in "025":
    print("<")
elif a + b in ["02", "25", "50"]:
    print(">")
elif a + b in ["20", "52", "05"]:
    print("<")
else:
    print("=")
