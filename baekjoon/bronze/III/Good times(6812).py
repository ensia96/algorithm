h, m = divmod(int(input()), 100)
t = h*60+m
for x, y in [(0, 'Ottawa'), (-180, 'Victoria'), (-120, 'Edmonton'), (-60, 'Winnipeg'), (0, 'Toronto'), (60, 'Halifax'), (90, "St. John's")]:
    h, m = divmod(t+x, 60)
    print(f"{h%24 or''}{m:02} in", y)
