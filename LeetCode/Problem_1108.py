def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    chars = [char for char in address]
    i = 0
    while i < len(chars): 
        if chars[i] == ".": 
            chars.insert(i+1, "]")
            chars.insert(i, "[")
            i += 1
        i += 1
    return "".join(chars)