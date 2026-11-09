class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        key = {}
        for l in s1:
            key[l] = key.get(l,0) + 1
        i  = 0
        correct = len(key)
        print(s2)
        while i< len(s1):
            print(i)
            print(s2[i])
            if s2[i] in key:
                key[s2[i]] -=1
                if key[s2[i]] == 0:
                    correct-=1
                if key[s2[i]] == -1:
                    correct+=1
            i+=1
        if correct == 0:
            return True

        l = 0
        while i < len(s2):
            if s2[i] in key:
                key[s2[i]] -=1
                if key[s2[i]] == 0:
                    correct-=1
                if key[s2[i]] == -1:
                    correct+=1
            if s2[l] in key:
                if key[s2[l]] == 0:
                    correct+=1
                key[s2[l]] +=1
                if key[s2[l]] == 0:
                    correct-=1
            if correct == 0:
                return True
            i+=1
            l+=1
            print(key)
            
 

        return False
            

        