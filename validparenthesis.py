def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    def split(word):
        return [char for char in word]

    bracketsdict = {
        '(': 'N',
        '[': 'N',
        '{': 'N',
        ')': '(',
        ']': '[',
        '}': '{'
    }
    sl = split(s)
    if len(sl)%2 != 0:
        return False
    else:
        stack = []
        a = 0
        while a < len(sl):
            if stack == []:
                stack.append(sl[a])
                a+=1
            else:
                if stack[-1] == bracketsdict[sl[a]]:
                    del stack[-1]
                    a+=1
                else:
                    stack.append(sl[a])
                    a+=1
        if stack == []:
            return True
        return False
print(isValid("[({(())}[()])]"))