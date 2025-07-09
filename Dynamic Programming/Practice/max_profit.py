def max_profit(stock_prices: list[int]):
    max_profit = 0

    # If there are no stock prices or only 1 stock price, the profit will be 0 as no transactions have been made.
    if len(stock_prices) < 2:
        return max_profit

    # Start with the first day as the buy day and the second as the sell day, because we must buy (or purchase) a stock before we can sell it.
    buy_index = 0
    sell_index = 1

    while sell_index < len(stock_prices):
        # Calculate profit if we were to sell on the current sell day.
        current_profit = stock_prices[sell_index] - stock_prices[buy_index]

        # Check if there is a better profit made.
        if current_profit > max_profit:
            max_profit = current_profit

        # Check if the current sell price is lower than the current buy price. This means there is a new better day to buy the stock for a lower price.
        if stock_prices[sell_index] < stock_prices[buy_index]:
            buy_index = sell_index

        # Continue to the next day, to calculate the profit made when the stock is sold on the next day.
        sell_index += 1

    return max_profit


stock_prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(stock_prices)
print("Test with mixed stock prices:")
print("Prices:", stock_prices)
print("Maximum profit:", profit)
print("-----------------------------")


stock_prices = [7, 6, 4, 3, 1]
profit = max_profit(stock_prices)
print("Test with descending stock prices:")
print("Prices:", stock_prices)
print("Maximum profit:", profit)
print("-----------------------------")


stock_prices = [1, 2, 3, 4, 5, 6]
profit = max_profit(stock_prices)
print("Test with ascending stock prices:")
print("Prices:", stock_prices)
print("Maximum profit:", profit)
print("-----------------------------")


"""
    EXPECTED OUTPUT:
    ----------------
    Test with mixed prices:
    Prices: [7, 1, 5, 3, 6, 4]
    Maximum profit: 5
    -----------------------------
    Test with descending prices:
    Prices: [7, 6, 4, 3, 1]
    Maximum profit: 0
    -----------------------------
    Test with ascending prices:
    Prices: [1, 2, 3, 4, 5, 6]
    Maximum profit: 5
    -----------------------------

"""
