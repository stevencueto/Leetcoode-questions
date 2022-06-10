class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevMap = {}
        
        for i, n  in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[n] = i
            
            
            ## make a hash map, store the values once, then check if the difference of the subsctraction equals to the target
            ##if so, then return the index for them, else store into hash map.