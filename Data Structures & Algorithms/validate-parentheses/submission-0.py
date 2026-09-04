class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(','}':'{',']':'['}

        for char in s:
            if char in pairs:  # closers
                if not stack or pairs[char] != stack.pop():
                    return False 

            else: # openers
                stack.append(char)
        
        return not stack