def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    my_set = set()
    for num in nums: 
        length = len(my_set)
        my_set.add(num)
        if len(my_set) == length:
            return True
    return False
