class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:  
                target = n + nums[l] + nums[r]

                if target < 0:
                    l += 1
                elif target > 0:
                    r -= 1
                else:
                    output.append([n , nums[l] , nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return output
    
    """
    so we are going to aproach this by first sorting the input, then we are going to enter a for loop, with the index and the element at the index, after that we are going to check if the number we want to enter in the other nested loop is the same as the previous one, we are going to the next iteration, then afert that we are going to use binary search, if we have a matching target we append it to the output and increment our left pointer if the value at the left pointer is the same as the value at the right pointer we are going to increase left until we have a different value and keep in mind that left must not be larger or eaual to right, if the sum is larger then we are going to decremet right, else we increment left, time complexity is going to be O(n2) because we have 2 nested loops, and space complexity is O(n) because we have to use the sorting method which uses extra memory.
    """