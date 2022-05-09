def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy = 0
    sell = 1
    max_profit = 0
    while sell < len(prices):
        if prices[sell] - prices[buy] > max_profit:
            max_profit = prices[sell] - prices[buy]
        if prices[buy] > prices[sell]: 
            buy = sell   
        sell += 1
    return max_profit