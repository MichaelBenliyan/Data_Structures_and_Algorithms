def maxProduct(nums):
    def compare_max(max_product, *nums): 
        if max_product is None: 
            max_product = nums[0]
        for num in nums: 
            max_product = max(max_product, num)
        return max_product
    i = 0 
    max_product = None
    always_counter = None
    after_first_negative_counter = None
    first_negative = False
    while i < len(nums): 
        num = nums[i]
        if num == 0: 
            max_product = compare_max(max_product, 0)
            first_negative = False
            always_counter = None
            after_first_negative_counter = None
        else: 
            if not first_negative: 
                if num < 0: 
                    first_negative = True
                if always_counter is None: 
                    always_counter = num
                else: 
                    always_counter *= num
                max_product = compare_max(max_product, always_counter)
            else: 
                if after_first_negative_counter is None: 
                    after_first_negative_counter = num 
                else: 
                    after_first_negative_counter *= num 
                always_counter *= num 
                max_product = compare_max(max_product, always_counter, after_first_negative_counter)
        i += 1
    return max_product