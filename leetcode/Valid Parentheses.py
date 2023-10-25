class Solution(object):
    def isValid(self, s):
        a,b = [], {')':'(', ']':'[','}':'{'}
        for i in s:
            if i in b:
                if not(a and a.pop() == b[i]):
                    return False
            else:
                a.append(i)
        return not a