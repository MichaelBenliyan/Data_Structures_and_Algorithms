def find_corrupt_pair(nums): 
    i = 0
    while i < len(nums): 
        j = nums[i] - 1
        if nums[i] != nums[j]: 
            nums[i], nums[j] = nums[j], nums[i]
        else: 
            i += 1

    solution = []
    for i in range(len(nums)): 
        if nums[i] != i+1: 
            solution.append(nums[i])
            solution.append(i+1)
    return solution


print(find_corrupt_pair([3, 1, 2, 3, 6, 4]))
