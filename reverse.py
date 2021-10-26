from struct import pack, error
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    def test_32bit(n):
        try:
            pack("i", n)
        except error:
            return False
        return True

    numarray = [str(x) for x in str(x)]
    if numarray[0] == "-":
        result = "-"
        i = 1
        stack1 = []
        while i < len(numarray):
            stack1.append(numarray[i])
            i += 1
        j = 1
        while j < len(numarray):
            element = stack1.pop()
            element = str(element)
            result += element
            j += 1
    else:
        result = ""
        k = 0
        stack2 = []
        while k < len(numarray):
            stack2.append(numarray[k])
            k += 1
        l = 0
        while l < len(numarray):
            element = stack2.pop()
            element = str(element)
            result += element
            l += 1
    result = int(result)
    if test_32bit(result) == False:
        return 0
    return result
    
print(reverse(-1563847412))
