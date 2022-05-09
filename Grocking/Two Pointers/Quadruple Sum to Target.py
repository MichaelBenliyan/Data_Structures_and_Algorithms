def qstt(nums, target): 
    nums.sort()
    all_solutions = []
    i = 0 
    while i < len(nums) - 3: 
        if i>0 and nums[i] == nums[i-1]: 
            i += 1
            continue
        j = i+1
        while j < len(nums) - 2:
            if nums[j] == nums[j-1]: 
                j += 1
                continue 
            new_target = target-nums[i]-nums[j]
            new_solutions = perform_check(nums, new_target, i, j)
            for solution in new_solutions: 
                all_solutions.append(solution)
            j += 1
        i += 1
    return all_solutions
    
        
def perform_check(nums, target, i, j):
    valid_ans = []
    num1, num2 = nums[i], nums[j]
    left, right = j+1, len(nums)-1
    while left < right: 
        if nums[left] + nums[right] == target: 
            valid_ans.append([num1, num2, nums[left], nums[right]])
            og_left = nums[left]
            while nums[left] == og_left and left < len(nums) - 1: 
                left += 1
        elif nums[left] + nums[right] > target: 
            right -= 1
        else: #nums[left] + nums[right] < target
            left += 1
    return valid_ans
        
print(qstt([4, 1, 2, -1, 1, -3], 1))
print(qstt([2, 0 , -1, 1, 1, 1, 1, -2, 2], 2))