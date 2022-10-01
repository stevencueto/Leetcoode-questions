class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        
        for i in nums:
            hs[i] = hs.get(i, 0) + 1
        
        for n, c in hs.items():
            freq[c].append(n)
        
        output = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output
                
                
                """
                t O (n), s O(n)                """