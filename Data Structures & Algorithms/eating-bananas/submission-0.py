class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # each element in the array is number of bananas
        # piles[i] -> number of bananas
        # h is number of hours to eat the bananas
        # bananas eated per hour -> k

        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right)//2
            hours = 0
            for i in range(len(piles)):
                if  piles[i] % mid == 0:
                    hours = hours + (piles[i] // mid)
                else:
                    hours = hours + (piles[i]//mid) + 1
                    
            if hours <= h:
                right = mid
            else:
                left = mid+1
        return left

        
        
