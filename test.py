def depositProfit(deposit, rate, threshold):
    year = 0
    while True:
        deposit += deposit * rate / 100
        year += 1
        if deposit >= threshold:
            break
    return year


print(depositProfit(100, 20, 170))
# => should return 3
