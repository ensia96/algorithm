n = input()
i = 0
while len(n) > 1:
    n = f"{eval('*'.join(n))}"
    i += 1
print(i)
