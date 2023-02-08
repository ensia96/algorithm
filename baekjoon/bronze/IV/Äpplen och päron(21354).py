a, b = map(int, input().split())
a, b = a*7, b*13
print(['Petra', 'Axel', 'lika'][(a > b)+2*(a == b)])
