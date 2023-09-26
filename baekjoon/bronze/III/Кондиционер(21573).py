a, b = map(int, input().split())
c = input()
print([a, b][(c == 'freeze')*(a > b)+(c == 'heat')*(a < b)+(c == 'auto')])
