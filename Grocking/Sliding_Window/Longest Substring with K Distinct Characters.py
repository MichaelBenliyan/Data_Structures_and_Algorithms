def lswkdc(string, k): 
    counter = {}
    answer = 0
    left = 0
    right = 0
    while right < len(string): 
        while len(counter.keys()) <= k: 
            if not counter.get(string[right]): 
                counter[string[right]] = 1
            else: 
                counter[string[right]] += 1
            right += 1
        answer = max(answer, right-left-1)
        counter[string[left]] -= 1
        if counter[string[left]] == 0: 
            del counter[string[left]]
        left += 1
    return answer

print(lswkdc("cbbebi", 3))