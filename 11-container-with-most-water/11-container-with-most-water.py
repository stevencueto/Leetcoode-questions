class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        output = 0
        
        while l < r:
            curr = min(height[l], height[r]) * (r - l)
            output = max(output, curr)
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return output
    
    
    """
    
    this solution is O(n) and O(1)
    """