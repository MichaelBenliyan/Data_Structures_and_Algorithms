def removeVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    answer = ""
    vowels = "aeiou"
    for letter in s: 
        if letter in vowels: 
            pass
        else: 
            answer += letter
    return answer