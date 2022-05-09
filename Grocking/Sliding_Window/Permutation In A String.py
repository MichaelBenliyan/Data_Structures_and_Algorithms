def permutaion_in_a_string(string, pattern): 
    pattern_map = {}
    window_map = {}
    window_start = 0
    output = False
    for char in pattern:
        if char not in pattern_map: 
            pattern_map[char] = 0
        pattern_map[char] += 1
    
    for window_end in range(len(string)): 
        starting_char = string[window_start]
        cur_char = string[window_end]
        
        if cur_char not in window_map: 
            window_map[cur_char] = 0
        window_map[cur_char] += 1
        
        if window_end - window_start + 1 < len(pattern): 
            pass
        elif window_end - window_start + 1 == len(pattern): 
            if window_map == pattern_map: 
                return True
        else: 
            window_map[starting_char] -= 1
            if window_map[starting_char] == 0: 
                del window_map[starting_char]
            window_start += 1 
            if window_map == pattern_map: 
                return True
    
    if window_end - window_start == len(pattern): 
        if window_map == pattern_map: 
            return True
    return False
        
print(permutaion_in_a_string("aaacb", "abc"))