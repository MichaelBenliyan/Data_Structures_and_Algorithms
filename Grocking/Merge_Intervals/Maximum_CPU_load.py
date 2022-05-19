def maximum_cpu_load(jobs): 
    left, right = 0, 1
    start, end, cpu = 0, 1, 2
    jobs.sort(key=lambda x: x[start])
    max_cpu, current_cpu = 0, jobs[left][cpu]
    
    while right < len(jobs): 
        while right < len(jobs) and jobs[right][start] < jobs[left][end]: 
            current_cpu += jobs[right][cpu]
            right += 1
            max_cpu = max(max_cpu, current_cpu)
        if right >= len(jobs): 
            break
        while left < len(jobs) and jobs[left][end] < jobs[right][start]: 
            current_cpu -= jobs[left][cpu]
            left += 1
    return max_cpu

print(maximum_cpu_load([[1,4,3], [2,5,4], [7,9,6]]))
print(maximum_cpu_load([[6,7,10], [2,4,11], [8,12,15]]))
print(maximum_cpu_load([[1,4,2], [2,4,1], [3,6,5]]))