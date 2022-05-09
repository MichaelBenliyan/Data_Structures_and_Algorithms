def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    def fibonaci(n): 
        total = 0
        for i in range(1, n): 
            total += i
        return total
    
    good_pairs = 0
    value_count = {}
    for num in nums: 
        if value_count.get(num): 
            value_count[num] += 1
        else: 
            value_count[num] = 1
    for count in value_count.values(): 
        if count > 1: 
            good_pairs += fibonaci(count)
    return good_pairs