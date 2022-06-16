class Solution:
    def hammingWeight(self, n: int) -> int:
        
    ### more efficient one would be using this trick too only count the ones inside the n:
    
        ans = 0 
        while n:
            n &= (n - 1)
            ans += 1
        return ans


    """this uses bit manipulation with shifting from the bit with the >> 1, we update the value of the n, we only increment n when the remainder is = 1 and we shift the bits, because is more cpu efficient, if we find n = 0, return the output, time complexity is O(1) the max the while lop can run is 32 times, space complexity O(i)"""
    
#     ans = 0
        
#         while n:
#             ans += n % 2
#             n = n >> 1
#         return ans