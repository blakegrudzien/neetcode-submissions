class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i, t in enumerate(temperatures): 
            while stack and stack[-1][0] < t:
                _, index = stack.pop()
                temperatures[index] = i-index
            stack.append([t,i])

        for _,i in stack:
            temperatures[i] = 0
        return temperatures 

        