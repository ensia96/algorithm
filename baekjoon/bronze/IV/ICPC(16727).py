a, b = map(int, input().split())
c, d = map(int, input().split())
x, y = 'Persepolis', 'Esteghlal'
print(x if a+d > b+c else y if a+d < b +
      c else x if d > b else y if d < b else 'Penalty')
