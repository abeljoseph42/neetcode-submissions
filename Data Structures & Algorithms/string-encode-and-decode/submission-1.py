class Solution:

    def encode(self, strs: List[str]) -> str:
        mystr = ""
        for i in range(len(strs)):
            mystr += str(len(strs[i])) + '#' + strs[i]
        return mystr

    def decode(self, s: str) -> List[str]:
        mylist = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            mylist.append(s[i:j])
            i = j
        return mylist
