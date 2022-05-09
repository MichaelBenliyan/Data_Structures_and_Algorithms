def mws(nums): 
    low, high = 0, len(nums) - 1
    
    #find the first out of sort on left side
    while low < len(nums)-1 and nums[low] < nums[low+1]: 
        low += 1
        
    #if true, list is sorted
    if low == len(nums) - 1: 
        return 0
    
    while high > 0 and nums[high] >= nums[high-1]: 
        high -= 1
    
    largest, smallest = nums[low], nums[low]
    for i in range(low, high+1): 
        largest = max(nums[i], largest)
        smallest = min(nums[i], smallest)
    
    while low > 0 and nums[low-1] > smallest:
        low-=1
    
    while high < len(nums)-1 and nums[high+1] < largest:
        high += 1
        
    return high-low+1
    
    
    
        
    
    
       
print(mws([1, 3, 2, 0, -1, 7, 10]))
print(mws([1, 3, 2, 0, -1, 7, 10]))
print(mws([1, 2, 3]))
print(mws([3, 2, 1]))