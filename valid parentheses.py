class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closepara = {')':'(' , ']':'[' , '}':'{'}
        for i in s:
            if i in closepara:
                if stack and stack[-1]==closepara[i]:
                    stack.pop()
                else :
                    return False
            else :
                stack.append(i)
        return True if stack == [] else False
