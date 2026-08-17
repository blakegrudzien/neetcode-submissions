class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        current = []
        final = []
        used = set()

        def helper(current, final, used):
            if len(current) == len(nums):
                final.append(current)
                return
            for i in nums:
                if i not in used:
                    temp_cur = current.copy()
                    temp_used = used.copy()
                    temp_cur.append(i)
                    temp_used.add(i)
                    helper(temp_cur, final, temp_used)

        helper(current,final,used)
        return final