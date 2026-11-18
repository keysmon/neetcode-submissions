class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        openToClose = { "(" : ")", "[" : "]", "{" : "}" }

        for c in s:
            if c in openToClose:
                stack.append(c)
            else:
                if not stack or openToClose[stack.pop()] != c:
                    return False
        return len(stack) == 0
                    