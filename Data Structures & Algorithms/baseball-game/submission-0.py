class Solution:
    def calPoints(self, operations: List[str]) -> int:
        key = []
        total = 0
        for val in operations:
            if val == "+":
                key.append(str(int(key[-1])+ (int(key[-2]))))
                total+= int(key[-1])
            
            elif val == "D":
                key.append(str(int(key[-1])*2))
                total+= int(key[-1])

            elif val == "C":
                total-= int(key[-1])
                key.pop()
                

            else:
                key.append(val) 
                total+= int(key[-1])
        return total
        