class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(','}':'{',']':'['}

        for char in s:
            if char in pairs: # closer
                if not stack or pairs[char] != stack.pop():
                    return False

            else: # opener
                stack.append(char)
        return not stack

       