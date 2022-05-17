def smallest_missing_positive_number(nums): 
    positive_nums = set()
    max_num = 0
    for num in nums: 
        if num > 0: 
            positive_nums.add(num)
            max_num = max(max_num, num)

    for i in range(1, max_num+2): 
        if i not in positive_nums:
            return i
    

print(smallest_missing_positive_number([33, 37, 5]))

