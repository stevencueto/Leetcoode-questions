class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs = set()
        
        for n in nums:
            if n in hs:
                return True
            hs.add(n)
        
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        """
        make a hash map, loop through the array, if we find an existing value, return false, else at the end of the loop return true
        """