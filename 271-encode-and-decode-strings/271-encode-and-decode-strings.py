class Codec:
    def encode(self, s: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        
        for i in s:
            res += str(len(i)) + "#" + i
        
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res, i = [] ,  0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j + 1 + length])
            i = j + 1 + length
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))