a, x, b, y, c, f = *input().split(), lambda x, y, z: [eval(f"abs({x})//abs({z})")*(
    1-2*(eval(f"{x}*{z}") < 0)), eval(f"{x}{y}{z}")][y in '+-*']
print(*sorted([f(f(a, x, b), y, c), f(a, x, f(b, y, c))]))
