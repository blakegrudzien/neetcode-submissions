class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        for first, second in prerequisites:
            if first not in courses:
                courses[first] = []
            courses[first].append(second)

        print(courses)

        def dfs(curr, cycle):
            
            if curr in cycle:
                print("cycle found")
                return False
            if curr not in courses or courses[curr] == []:
                return True
            

            cycle.add(curr)
            for before in courses[curr]:
                if not dfs(before, cycle):
                    return False
            cycle.remove(curr)
            courses[curr] = []
            return True
 

        cycle = set()
        for start in courses.keys():
            cycle.clear()
            if not dfs(start, cycle):
                return False
        return True

            
        