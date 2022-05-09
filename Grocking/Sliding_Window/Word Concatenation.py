def word_concatentation(string, words): 
    words_set = set()
    window_set = set()
    for word in words: 
        words_set.add(word)
    
    window_start = 0
    word_start = 0
    solution = []
    
    window_end = 3
    while window_end < len(string): 
        while string[word_start:window_end] in words_set and string[word_start:window_end] not in window_set: 
            window_set.add(string[word_start:window_end])
            word_start += 3
            window_end += 3
        if window_set == words_set: 
            solution.append(window_start)
        window_set = set()
        window_start += 3
        word_start = window_start
        window_end = window_start + 3
    return solution
            
print(word_concatentation("catcatfoxfox", ["cat", "fox"]))