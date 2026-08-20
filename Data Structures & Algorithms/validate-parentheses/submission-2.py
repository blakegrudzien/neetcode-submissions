class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {'(': ')', '{': '}', '[': ']', }
        i = 0

        for l in s:
            if l in key:
                stack.append(l)
            elif l in key.values():
                if stack and key[stack[-1]] == l:
                    stack.pop()
                else:
                    return False

        if stack: 
            return False
        return True

        