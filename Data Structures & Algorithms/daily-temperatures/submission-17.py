class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                p_temp, p_index = stack.pop()
                days[p_index] = i-p_index
            stack.append([t,i])
        return days
        