x = ''
for l in open(0):
    i = l.strip()
    if i.isdigit():
        x = f'{int(eval(x+i))}'
    if i in '+-*/':
        x += i
print(x)
