class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while(l <= r):
            mid = l + math.floor((r - l ) / 2)
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1
    
    """
    make 2 pointers, then use them to loop throgh the array given, start in the middle point, if the starting point is less than targert, increment l by mid + 1, else decrement r by mid - 1, if we exit the loop, return negative
    """