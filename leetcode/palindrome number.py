class Solution(object):
    def isPalindrome(self, x):
        x1 = [i for i in str(x)]
        if x1[::-1] == x1:
            return True
        else:
            return False