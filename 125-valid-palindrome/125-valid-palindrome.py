class Solution(object):
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        #make a 2 pointer funcion to loop through, then check if the char is alphanumerical, then is it is, compare, if they match increment left, decrement right, if they dont return False, do this untile l is not overlapping r.
        
        while(l < r):
            while l < r and not self.is_alph_num(s[l]):
                l += 1
            while r > l and not self.is_alph_num(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                print(s[l])
                print(s[r])
                return False
            l = l + 1
            r = r - 1
        
        return True
        
    def is_alph_num(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or 
               ord("a") <= ord(c) <= ord("z") or 
               ord("0") <= ord(c) <= ord("9"))
    #this helper function is to make sure 