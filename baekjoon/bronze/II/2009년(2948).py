d, m = map(int, input().split())
print(["Wednes", "Thurs", "Fri", "Satur", "Sun", "Mon", "Tues"][(
    sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:m-1])+d) % 7]+'day')
