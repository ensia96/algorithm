a, b, c, d, e = map(int, input().split())
print(*min((a * i + c * (j := -((b * i - e) // d)), j, i)
      for i in range(e // b + 1))[::-1])
