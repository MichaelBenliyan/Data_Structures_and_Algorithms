def mws(nums): 
    start, end = None, None
    i = 0 
    while i < len(nums): 
        if i == 0: 
            i += 1
        elif nums[i] > nums[i-1]: 
            i += 1
        else: 
            if start is None: 
                start = i 
            else: 
                end = i
            i += 1
    if start is None: 
        return 0
    else: 
        return end-start+1

print(mws([1, 3, 2, 0, -1, 7, 10]))