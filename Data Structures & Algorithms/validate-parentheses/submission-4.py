class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        mapped = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in mapped:
                if not q or q[-1] != mapped[c]:
                    return False
                q.pop()
            else:
                q.append(c)

        if not q:
            return True
        else:
            return False
