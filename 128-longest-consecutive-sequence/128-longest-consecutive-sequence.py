class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ### make a set of the nums, then we are going to loop throght the nums, number we're at does not belong in a sequence nums[i] - 1 is not in the set, then we check the lenght of the consecutive subarray, 
        nSet = set(nums)
        output = 0
        
        for n in nums:
            if n - 1 not in nSet:
                length = 1
                while (n + length) in nSet:
                    length += 1
                output = max(length, output)
        
        return output