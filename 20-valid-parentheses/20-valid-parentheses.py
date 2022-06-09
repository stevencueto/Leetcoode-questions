class Solution(object):
    def isValid(self, s):
        stack = []
        closing_string = { 
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for i in s:
            if i in closing_string:
                if stack and stack[-1] == closing_string[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        return True if not stack else False