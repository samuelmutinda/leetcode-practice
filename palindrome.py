def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    def split(word):
        return [char for char in word]

    if x < 0:
        return False
    digitarray = split(str(x))
    xstring = str(x)
    if len(digitarray)%2 == 0:
        b = int((len(digitarray)/2) - 1)
        right = ""
        left = xstring[0:b+1]
        i = len(digitarray) - 1
        while i > b:
            right += digitarray[i]
            i -= 1
        if right == left:
            return True
        return False
    else:
        mid = int(len(digitarray)/2)
        right = ""
        left = xstring[0:mid]
        j = len(digitarray) - 1
        while j > mid:
            right += digitarray[j]
            j -= 1
        if right == left:
            return True
        return False
    
print(isPalindrome(120021))
