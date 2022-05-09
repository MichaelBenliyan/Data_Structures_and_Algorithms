def finalValueAfterOperations(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    x = 0
    for string in operations: 
        if "++" in string: 
            x += 1
        elif "--" in string: 
            x -= 1
    return x