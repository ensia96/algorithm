a = [*input() * 99]
[print(end=chr((ord(a.pop(0)) + ord(c)) % 26 + 65))for c in input()if c > '@']
