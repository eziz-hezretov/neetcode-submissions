class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = list(s)
        stack = []

        for bracket in brackets:
            if bracket in '([{':
                stack.append(bracket)
            if not stack:
                return False
                break
            elif bracket == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
                    break
            elif bracket == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
                    break
            elif bracket == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
                    break

        if not stack:
            return True
        else:
            return False
       
            
            