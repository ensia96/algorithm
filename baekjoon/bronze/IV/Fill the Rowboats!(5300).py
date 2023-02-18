n, g = int(input()), 'Go!'
print(*([i+1, f'{i+1} {g}'][i % 6 == 5 or n-i == 1]for i in range(n)))
