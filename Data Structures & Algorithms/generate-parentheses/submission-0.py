class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []


        def helper(current, left, right, answer):
            if max(left,right) == 0:
                answer.append(current)
            if left < right:
                right_copy = current + ')'
                helper(right_copy, left, right-1, answer)
            if left == 0:
                return
            left_copy = current + '('
            helper(left_copy, left-1, right, answer)
        helper('',n,n,answer)
        return answer
                

        