class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # s-> dic1 = {'r':2,'a':1,'c':2, 'e':1} 
        # t-> dic2 = {'c':1, 'a':2, 'r':2, 'e':1}
        # if s[r] in t[r]: 
        if len(s)!=len(t):
            return False
        dic1 = {}
        dic2 = {}

        # we know that lengths of both strings are same, so:
        for i in range(len(s)):
            dic1[s[i]] = 1 + dic1.get(s[i], 0)
            dic2[t[i]] = 1 + dic2.get(t[i], 0)
        return dic1 == dic2

        