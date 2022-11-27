input()
print(int(''.join(sorted(input().split(), key=lambda x: (x*11)[:10])[::-1])))
