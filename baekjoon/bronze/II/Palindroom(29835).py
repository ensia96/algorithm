input()
s = input()
print(sum(map(str.__gt__, s, r := s[::-1])))
print(*map(min, s, r), sep='')
