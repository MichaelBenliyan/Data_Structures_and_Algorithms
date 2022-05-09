from tracemalloc import start


def sswags(array, target): 
    start = 0
    end = 1
    sum = array[0]
    answer = None
    while end < len(array): 
        sum += array[end]
        while sum >= target and start < len(array):
            subarray = end-start+1
            if answer is None or subarray < answer: 
                answer = subarray
            sum -= array[start]
            start += 1
        end += 1
    if answer is None: 
        return 0
    return answer

print(sswags([3, 4, 1, 1, 6], 8 ))
            