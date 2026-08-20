class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for s in sandwiches:
            count = 0
            while students[0] != s:
                print(students)
                count+=1
                if count == len(students):
                    return count 
                students.append(students[0])
                students.pop(0)
            students.pop(0)

            
        return 0
                
            

        