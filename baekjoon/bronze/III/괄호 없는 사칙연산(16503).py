a, x, b, y, c = input().split()


def f(x, y, z): return str(
    eval([f"abs({x}){y}abs({z})*(1-2*({x}*{z}<0))", x+y+z][y in '+-*']))


print(*sorted([f(f(a, x, b), y, c), f(a, x, f(b, y, c))]))
