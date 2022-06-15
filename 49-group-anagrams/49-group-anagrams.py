class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            output[tuple(count)].append(s)
        return output.values()
    
    
    #T O(m * n solution), S O(n)
    
    """
    make a default dict, so we can store the output, then make a for loop to go through all the strings, then another one to loop through each char, then we are going to use the ASCII value of the string to make it into a touple with keys and a list the the strings that match the values of the count for the ASCII value. return the values only as the outpout
    """