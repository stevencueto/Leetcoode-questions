class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hs = {}
        l, res, maxf = 0, 0, 0
        
        for r in range(len(s)):
            hs[s[r]] = hs.get(s[r], 0) + 1
            maxf = max(maxf, hs[s[r]])
            
            if (r - l + 1) - maxf > k:
                hs[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
            
        return res
    
    
    #make a sliding window, update pointers, keep the max frequency, if the window minus the max freq is > than k, decrement s[l] - 1, increment l to move the window, update res, return res O(n) O(1)