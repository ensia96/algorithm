n = int(input())
print(max((min(n+8, 210), 1), (min(n+4, 220), 2),
      (min(n+2, 230), 3), (min(n+1, 240), 4))[1])
