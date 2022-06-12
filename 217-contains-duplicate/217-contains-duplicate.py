class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs = {}
        
        for n in nums:
            if hs.get(n):
                return True
            hs[n] = 1
        
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        """
        make a hash map, loop through the array, if we find an existing value, return false, else at the end of the loop return true
        """