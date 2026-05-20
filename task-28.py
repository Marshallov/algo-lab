def find_best_trade(prices):
    if not prices or len(prices) < 2:
        return "Перепродажа с прибылью невозможна"

    min_price = prices[0]
    min_day = 1
    
    max_profit = 0
    best_buy = None
    best_sell = None

    for i in range(1, len(prices)):
        current_day = i + 1
        current_price = prices[i]

        if current_price < min_price:
            min_price = current_price
            min_day = current_day
        else:
            current_profit = current_price - min_price
            if current_profit > max_profit:
                max_profit = current_profit
                best_buy = min_day
                best_sell = current_day

    if max_profit > 0:
        return f"Покупать в день {best_buy}, продавать в день {best_sell}"
    
    return "Перепродажа с прибылью невозможна"

# Пример 1

prices_1 = [9, 1, 5]
print(find_best_trade(prices_1))

# Пример 2

prices_2 = [10, 8, 6, 4, 2]
print(find_best_trade(prices_2))

# Пример 3

prices_3 = [3, 2, 6, 1, 4, 9, 5]
print(find_best_trade(prices_3))