class Solution:
    def isPalindrome(self, s: str) -> bool:
        myStr = s.replace(" ", "")
        n = len(myStr)
        i = 0
        j = n - 1

        while i < j:
            while not myStr[i].isalnum() and i < j:
                i += 1
            while not myStr[j].isalnum() and i < j:
                j -= 1
            
            if myStr[i].lower() != myStr[j].lower():
                return False
            i += 1
            j -= 1
            
        return True
