class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i,char in enumerate(s):
            if char in "{[(":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top_char = stack.pop()
                if top_char == "{" and char == "}":
                    continue
                elif top_char == "(" and char == ")":
                    continue
                elif top_char == "[" and char == "]":
                    continue
                else:
                    return False
        
        return len(stack) == 0
                
        