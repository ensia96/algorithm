a, b = map(int, input().split())
f, g = lambda a: 57*a*(30 < a) or (4+3*(5 < a)+5*(10 < a)+5*(20 < a))*100, lambda b: 90 + \
    90*b+(2 < b)*(10-5*b)+(5 < b)*(25-5*b) + \
    (20 < b)*(200-10*b)+(40 < b)*(600-15*b)
a //= 1000
b //= 1000
print(f'{(min(f(a), g(a))+min(f(b), g(b)))/100:.2f}')
