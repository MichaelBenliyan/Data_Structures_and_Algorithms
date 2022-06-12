class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1 
        m_i = ((end-start+1) // 2) + start
        while (end-start+1) > 3: 
            if nums[m_i] == target: 
                return m_i
            if nums[m_i] > nums[start]: #left sorted: greater than everything before 
                if nums[start] <= target <= nums[m_i]:  
                    end = m_i 
                else: 
                    start = m_i
                m_i = ((end-start+1) // 2) + start
            else:                       #right sorted: less than everything after 
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