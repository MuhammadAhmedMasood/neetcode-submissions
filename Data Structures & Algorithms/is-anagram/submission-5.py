class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

       # we can store each string in a dictionary and then 
       # compare both dict. If same, it will return True
       # otherwise, False. order doesnt matter in dict
       # we should also check whether both strings have same
       # length. if no same length then cant be equal
       # and we can return False directly

       if len(s) != len(t):
        return False

       pair1 = {}
       pair2 = {}

       for i in range(len(s)):
        pair1[s[i]] = 1 + pair1.get(s[i], 0)
        pair2[t[i]] = 1 + pair2.get(t[i], 0)
       return pair1 == pair2