import re
x, _, A = open(0)
print(re.subn(f'(?={x[:-1]})', x, A)[1])
