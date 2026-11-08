class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        courses = {}
        for i in range(numCourses):
            courses[i] = []

        for first, second in prerequisites:
            courses[first].append(second)
        flag = True

        res = []
        def dfs(curr, cycle): 
            if curr in cycle:
                return False
            if curr in visited: 
                return True
            if courses[curr] == []:
                if curr not in res:
                    res.append(curr)
                return True

            cycle.add(curr)
            for n in courses[curr]:
                if not dfs(n, cycle):
                    return False
            cycle.remove(curr)
            visited.add(curr)
            res.append(curr)
            return res




        cycle = set()
        visited = set()
        

        for c in courses.keys():
            cycle.clear()
            if not dfs(c,cycle):
                return []
        return res
        

            
            
            
        