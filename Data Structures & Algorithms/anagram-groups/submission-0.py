class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1 = defaultdict(list)
        for s in strs:
            count = [0]*26 # all small cases so 26 letters

            for c in s:
                count[ord(c) - ord("a")]+=1 # indexes a ->0 and z->25

            dict1[tuple(count)].append(s)

        return list(dict1.values())