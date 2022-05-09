def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_sum = nums[0]
    curr_sum = nums[0]
    i = 1
    while i < len(nums):
        if curr_sum > max_sum: 
            max_sum = curr_sum
        if nums[i] > curr_sum + nums[i]:
            curr_sum = nums[i]
        else: 
            curr_sum += nums[i]
        i+=1
    if curr_sum > max_sum: 
        max_sum = curr_sum
    return max_sum
