class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        pairs = {}
        result = 0

        for right in range(len(s)):
            pairs[s[right]] = pairs.get(s[right], 0) + 1

            while ( ((right-left+1) - max(pairs.values())) > k ):
                pairs[s[left]]-=1
                left+=1
            result = max(result, right - left + 1)
        return result