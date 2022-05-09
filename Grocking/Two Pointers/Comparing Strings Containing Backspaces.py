def cscb(string1, string2): 
    string1 = "".join(perform_backspaces(list(string1)))
    string2 = "".join(perform_backspaces(list(string2)))
    return string1 == string2
    
    
    
    
    
def perform_backspaces(string_list):
    i = len(string_list) - 1
    while i >= 0: 
        char = string_list[i]
        
        if char == "#": 
            j = i-1
            while string_list[j] == "#": 
                i -= 1
                j -= 1
            while i < len(string_list) and string_list[i] == "#": 
                string_list.pop(j)
                string_list.pop(j)
                j -= 1
                i -= 1
        i -= 1
    return string_list

print(cscb("xy#z", "xzz#"))
print(cscb("xy#z", "xyz#"))
print(cscb("xp#", "xyz##"))
print(cscb("xywrrmp", "xywrrmu#p"))