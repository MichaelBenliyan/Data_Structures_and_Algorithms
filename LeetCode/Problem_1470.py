def shuffle(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    i = n
    j = 1
    while i < len(nums): 
        nums.insert(j, nums[i])
        j += 2
        i += 2
    return nums[0:2*n]