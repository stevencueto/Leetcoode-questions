class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        l, r = 0 , len(nums) -1
        
        while l < r:
            if nums[l] + nums[r] == t:
                return [l + 1, r + 1]
            elif nums[l] + nums[r] < t:
                l += 1
            else:
                r -= 1 
            