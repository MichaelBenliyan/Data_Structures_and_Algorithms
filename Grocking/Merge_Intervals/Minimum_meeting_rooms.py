def minimum_rooms(intervals): 
    intervals.sort(key=lambda x: x[0])
    already_scheduled = set()
    start, end = 0, 1
    i = 0
    rooms = 0
    for i in range(len(intervals)): 
        if i in already_scheduled: 
            continue
        else: 
            already_scheduled.add(i)
            rooms += 1
            j = i
            results = check_for_more_rooms(j, intervals, already_scheduled, rooms)
            rooms = results["rooms"]
            already_scheduled = results["already_scheduled"]        
            
    return rooms        
            
def check_for_more_rooms(idx, intervals, already_scheduled, rooms): 
    result = {"already_scheduled": already_scheduled, "rooms": rooms}
    start, end = 0, 1
    current_end = intervals[idx][end]
    for i in range(idx+1, len(intervals)): 
        if i not in already_scheduled and current_end <= intervals[i][start]: 
            already_scheduled.add(i)
            result["already_scheduled"] = already_scheduled
            idx = i
            result = check_for_more_rooms(idx, intervals, already_scheduled, rooms)
            break
    return result
            
print(minimum_rooms([[4,5], [2,3], [2,4], [3,5]]))