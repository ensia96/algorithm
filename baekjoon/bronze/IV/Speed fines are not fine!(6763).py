n = -int(input())+int(input())
print(f'You are speeding and your fine is ${100 if n<21 else 270 if n<31 else 500}.'if n >
      0 else 'Congratulations, you are within the speed limit!')
