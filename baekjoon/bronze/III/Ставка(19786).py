f, F = lambda: map(int, input().split()), lambda r, g, b, x, y: x * \
    (r*r+g*g+b*b)+y*min([r, g, b])
for _ in ' '*int(input()):
    x, y = f()
    r, g, b = f()
    R, G, B = F(r+1, g, b, x, y), F(r, g+1, b, x, y), F(r, g, b+1, x, y)
    print('RED'if B <= R >= G else 'GREEN'if R <= G >= B else 'BLUE')
