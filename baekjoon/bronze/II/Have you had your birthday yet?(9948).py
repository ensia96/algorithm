for i in open(0):
    d = int(i[:2])
    if d == 0:
        break
    t = "Au" in i
    print(
        [
            [["Yes", "Happy birthday"][t and d == 4], "No"]["er" in i or t and d > 4],
            "Unlucky",
        ]["29 F" in i]
    )
