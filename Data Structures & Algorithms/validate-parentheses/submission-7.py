class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { ')':'(', '}':'{', ']':'['}

        stack = []

        for i in range(len(s)):
            curr = s[i]
            if curr in brackets:
                if stack and stack[-1] == brackets[curr]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(curr)
        
        return stack == []