def minimumSum(num):
    """
    :type num: int
    :rtype: int
    """
    num_s = str(num)
    num_a = list(num_s)
    num_a.sort()
    num_1 = ""
    num_2 = ""
    for n in num_a: 
        if len(num_1) == len(num_2): 
            num_1 += n
        else: 
            num_2 += n
    return int(num_1) + int(num_2)