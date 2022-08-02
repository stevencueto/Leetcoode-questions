class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            res += self.helper(i, i, s)
            res += self.helper(i, i + 1, s)
        return res
            
    def helper(self, l, r, s):
        res = 0
        
        while l >= 0 and r < len(s) and s[r] == s[l]:
            res += 1
            r += 1
            l -= 1
        return res
            