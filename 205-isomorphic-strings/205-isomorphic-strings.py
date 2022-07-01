class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charH1, charH2 = {}, {}
        
        for c1, c2 in zip(s, t):
            if ((c1 in charH1 and charH1[c1] != c2) or (c2 in charH2 and charH2[c2] != c1)):
                return False
            
            charH1[c1] = c2
            charH2[c2] = c1
            
        return True