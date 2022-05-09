def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    most_money = 0
    for account in accounts: 
        customer_total = 0
        for bank in account: 
            customer_total += bank
        most_money = max(most_money, customer_total)
    return most_money