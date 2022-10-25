class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        
        for i, n in enumerate(nums):
            dif = target - n
            if dif in hs:
                return [i, hs[dif]]
            else:
                hs[n] = i
        
            