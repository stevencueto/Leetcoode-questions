class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = 0
        maxSub = nums[0]
        
        for n in nums:
            if maxSum < 0:
                maxSum = 0
            maxSum += n
            maxSub = max(maxSub, maxSum)
            
        return maxSub