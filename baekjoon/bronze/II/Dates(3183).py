import datetime

for l in [*open(0)][:-1]:
    d, m, y = map(int, l.split())
    try:
        datetime.datetime(y, m, d)
        print("Valid")
    except:
        print("Invalid")
