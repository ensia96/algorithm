a, b, c = int(input()), int(input()), int(input())
print('Error'if 180-a-b-c else'Scalene'if a-b and b-c and c -
      a else'Equilateral'if a == b == c else'Isosceles')
