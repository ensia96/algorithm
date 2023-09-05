x, y = int(input()), int(input())
print(
    f'There are {sum(8-i<x for i in range(min(10,y)))} ways to get the sum 10.')
