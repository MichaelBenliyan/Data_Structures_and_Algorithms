def permutaion_in_a_string(string, pattern): 
    pattern_map = {}
    window_map = {}
    window_start, matches = 0, 0
    shortest_string_length = len(string) + 1
    shortest_string_start = 0
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
        
        if cur_char in pattern_map and window_map[cur_char] == pattern_map[cur_char]:
            matches += 1
        
        if matches == len(pattern_map): 
            while string[window_start] not in pattern_map or window_map[string[window_start]] -1 >= pattern_map[string[window_start]]: 
                if string[window_start] in pattern_map: 
                    window_map[string[window_start]] -= 1
                window_start += 1
            if window_end - window_start + 1 < shortest_string_length: 
                shortest_string_length = window_end-window_start + 1
                shortest_string_start = window_start
    
    solution = ""
    if shortest_string_length > len(string): 
        return solution
    for i in range(shortest_string_start, shortest_string_start+shortest_string_length):
        solution += string[i]
    return solution
        
print(permutaion_in_a_string("adcad", "abc"))