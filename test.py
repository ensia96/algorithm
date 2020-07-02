def maxProfit(prices):
    answer = []
    for i in range(1, len(prices)):
        if prices[i - 1] < prices[i]:
            print(prices[i] - prices[i - 1])
            answer.append(prices[i] - prices[i - 1])
    print(answer)

    print(
        sum(
            [
                prices[i] - prices[i - 1]
                for i in range(1, len(prices))
                if prices[i - 1] < prices[i]
            ]
        )
    )


# maxProfit([7, 1, 5, 3, 6, 4])
maxProfit([1, 2, 3, 4, 5])
# maxProfit([7, 6, 4, 3, 1])

# print(canJump([2, 3, 1, 1, 4]))
# => should return True

# print(canJump([3, 2, 1, 0, 4]))
# => should return False
