class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        for ch in s:
            if ch in pair:
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if pair[top] != ch:
                    return False
        if len(stack)==0:
            return True
        else:               
             return False