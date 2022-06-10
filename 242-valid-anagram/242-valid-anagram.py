class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        hs_s, hs_t = {}, {}
        
        for i in range(len(s)):
            hs_s[s[i]] = 1 + hs_s.get(s[i], 0)
            hs_t[t[i]] = 1 + hs_t.get(t[i], 0)
        for j in hs_s:
            if hs_s[j] != hs_t.get(j, 0):
                return False
        return True
    
    ## making the hashmap to loop through the strings, then store the char frequency, after that we take in the hs's and them we loop through them and compare the key values, if they don't match we return False, if at the end they match we return True time complexity is O(n or s+t cause he va to loop thorugh it all) space complexity is O(n or s + t) casue we need two hs