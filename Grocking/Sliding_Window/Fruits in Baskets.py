
def fruits(fruits): 
    num_fruits = 0
    fruit_ct = {}
    left = 0
    right = 0
    fruit1 = fruits[0]
    fruit2 = None 
    while right < len(fruits): 
        while fruits[right] == fruit1: 
            right += 1
            if fruit1 not in fruit_ct: 
                fruit_ct[fruit1] = 0
            fruit_ct[fruit1] += 1
        next_start = right
        fruit2 = fruits[right]
        fruit_ct[fruit2] = 1
        right += 1
        while right < len(fruits) and (fruits[right] == fruit1 or fruits[right] == fruit2):
            if fruits[right] == fruit1:
                fruit_ct[fruit1] += 1
            else: 
                fruit_ct[fruit2] += 1
            right += 1
        num_fruits = max(num_fruits, fruit_ct[fruit1] + fruit_ct[fruit2])
        if right == len(fruits): 
            return num_fruits
        fruit1 = fruits[next_start]
        fruit2 = None
        fruit_ct = {}
        left = next_start
        right = next_start
    return num_fruits

print(fruits(['A', 'B', 'C', 'A', 'C']))
