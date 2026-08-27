class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # sorted in non-decreasing order
        # e.g [1,1,1,2,3,4,5,6]
        # e.g [0,1,1,3]
        # numbers[left]+numbers[right] == target
        # return [numbers[left],numbers[right]]

        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
            elif numbers[left] + numbers[right] < target:
                left+=1
            else: #numbers[left] + numbers[right] > target:
                right-=1
