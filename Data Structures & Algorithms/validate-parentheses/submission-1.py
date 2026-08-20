class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {'(': ')', '{': '}', '[': ']', }
        i = 0

        for l in s:
            print(l)
            
            print(i)
            i+=1
            print(stack)
            if l in key:
                print("in keys")
                stack.append(l)
            elif l in key.values():
                if not stack:
                    return False
                if key[stack[-1]] == l:
                    stack.pop()
                else:
                    return False

        if stack: 
            return False
        return True

        