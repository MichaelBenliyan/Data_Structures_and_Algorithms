def maxArea( height):
    """
    :type height: List[int]
    :rtype: int
    """
    
    def max_area_is(max_area, length, height):
        area = length*height
        max_area = max(max_area, area)
        return max_area
    
    start = 0
    end = len(height) - 1
    max_area = 0
    
    while end > start:
        max_area = max_area_is(max_area, end-start, min(height[start], height[end]))
        if height[start] > height[end]: 
            end -= 1
        else: 
            start+=1
            
    return max_area
            