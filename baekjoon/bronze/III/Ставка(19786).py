f, F = lambda: map(int, input().split()), lambda r, g, b, y: (
    r*r+g*g+b*b)+y*min([r, g, b])
for _ in ' '*int(input()):
    x, y = f()
    r, g, b = f()
    R, G, B = F(r+1, g, b, y), F(r, g+1, b, y), F(r, g, b+1, y)
    print('RED'if B <= R >= G else 'GREEN'if R <= G >= B else 'BLUE')
