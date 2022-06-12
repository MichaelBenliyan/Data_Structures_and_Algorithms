class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1 
        m_i = ((end-start+1) // 2) + start
        while (end-start+1) > 3: 
            if nums[m_i] == target: 
                return m_i
            #left sorted: greater than everything before 
            if nums[m_i] > nums[start]: 
                if nums[start] <= target <= nums[m_i]:  
                    end = m_i 
                else: 
                    start = m_i
                m_i = ((end-start+1) // 2) + start
            #right sorted: less than everything after 
            else:                       
                if nums[m_i] <= target <= nums[end]: 
                    start = m_i
                else: 
                    end = m_i 
                m_i = ((end-start+1) // 2) + start
        options = [start, end, m_i]
        for option in options: 
            if nums[option] == target: 
                return option 
        return -1