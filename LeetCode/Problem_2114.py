def mostWordsFound(sentences):
    """
    :type sentences: List[str]
    :rtype: int
    """
    max_sentence = 0
    for sentence in sentences: 
        array = sentence.split(" ")
        max_sentence = max(max_sentence, len(array))
    return max_sentence