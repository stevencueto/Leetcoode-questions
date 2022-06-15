class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = collections.defaultdict(list)
        
        for s in strs:
            deck = [0] * 26
            for c in s:
                deck[ord(c) - ord('a')] += 1
            output[tuple(deck)].append(s)
        return output.values()