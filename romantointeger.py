def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    def split(word):
        return [char for char in word]
    
    chardict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    charlist = split(s)
    numlist = []
    a = 0
    while a < len(charlist):
        numlist.append(chardict[charlist[a]])
        a += 1
    number = 0
    b = 0
    while b < len(numlist):
        if b+1 < len(numlist):
            if numlist[b] < numlist[b+1]:
                number += numlist[b+1]
                number -= numlist[b]
                b += 2
            else:
                number += numlist[b]
                b += 1
        else:
            number += numlist[b]
            b += 1
    return number
print(romanToInt("XLIX"))