class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l, r = 0, len(nums) - 1
        
        while(l <= r):
            m = (l + r) // 2
            
            if nums[m] == t:
                return m
            elif nums[m] < t:
                l = m + 1
            else:
                r = m - 1
        return -1
    
    """
    make 2 pointers, then use them to loop throgh the array given, start in the middle point, if the starting point is less than targert, increment l by mid + 1, else decrement r by mid - 1, if we exit the loop, return negative
    """