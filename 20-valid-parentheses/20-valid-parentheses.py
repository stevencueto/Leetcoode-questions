class Solution(object):
    def isValid(self, s):
        stack = []
        closing_string = { 
            ")": "(",
            "}": "{",
            "]": "["
        }
        # check if we have a closing string, if we have one, check if we have a stack, if we have a stack then we have to check whether or not have a and then with the [-1] operator we get the last element added to the stack list, if so we pop it, else we return negative, because we have no matching string.
        for i in s:
            if i in closing_string:
                if stack and stack[-1] == closing_string[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        return True if not stack else False