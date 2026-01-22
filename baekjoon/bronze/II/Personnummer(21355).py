s = input()
print(f"{20 - ('+' in s) - (s[0] > '1')}" + s[:6] + s[7:])
