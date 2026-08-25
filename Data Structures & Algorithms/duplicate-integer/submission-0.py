class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        answer = {}
        for i, num in enumerate(nums):
            if num in answer:
                return True
            else:    
                answer[num] = i
        return False
        



        