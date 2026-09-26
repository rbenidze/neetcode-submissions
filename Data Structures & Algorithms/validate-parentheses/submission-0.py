class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for bracket in s:
            if bracket in close_to_open:
                if not stack or stack[-1] != close_to_open[bracket]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
                
        return not stack

