A = input()
print(*[a + b for a, b in zip(sorted(filter(str.isupper, A)),
      sorted(filter(str.isdigit, A))[::-1])], sep='')
