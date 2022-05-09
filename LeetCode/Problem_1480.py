def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    total = 0
    for num in nums: 
        total += num
        ans.append(total)
    return ans