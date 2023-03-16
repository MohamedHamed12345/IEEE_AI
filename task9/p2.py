def isalnum(s):return s.isalnum()
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=list(filter(isalnum,list(s.lower())))
        return s==s[::-1]