from unittest import skip


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    pointers = []
    merged = []
    solution = []
    start = 0
    for list in lists: 
        pointers.append(start)
        start += len(list) 
        for value in list:
            merged.append(value)
    while len(solution) < len(merged): 
        lowest_value = 10
        min_idx_pointer = []
        lowest_pointer = []
        
        i = 0
        while i < len(pointers): 
            if pointers[i] == "skip": 
                continue
            min_idx_pointer.append([i, pointers[i]])
            if merged[pointers[i]] < lowest_value: 
                lowest_value = merged[pointers[i]]
                lowest_pointer = [i, pointers[i]]
            i += 1
        solution.append(merged[lowest_pointer[1]])
        # if pointers[lowest_pointer[0]] + 1 > len(lists[lowest_pointer[0]]):
        #     pointers[lowest_pointer[0]] = "skip"
        # else: 
        pointers[lowest_pointer[0]] += 1
    return solution

print(mergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]]))
