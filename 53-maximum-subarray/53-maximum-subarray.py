class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        crr = 0
        output = nums[0]
        
        for n in nums:
            crr += n
            output = max(output, crr)
            if crr < 0:
                crr = 0
        return output
    
    
    """
    make a prefixed max subarray witrh index 0, the iterate through our list, if they sub array is larger then our max current sum, update it, if max sum is < 0, we waht to restart it's value
    """