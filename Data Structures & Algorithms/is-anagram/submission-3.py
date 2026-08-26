class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # s-> dic1 = {'r':2,'a':1,'c':2, 'e':1} 
        # t-> dic2 = {'c':1, 'a':2, 'r':2, 'e':1}
        # if s[r] in t[r]: 

        

        dic1 = {} # stores s
        dic2 = {} # stores t
        if len(s) != len(t):
            return False
        for value_s in s:
            if value_s in dic1:
                dic1[value_s]+=1 
            else:
                dic1[value_s] = 1
        for value_t in t:
            if value_t in dic2:
                dic2[value_t]+=1 
            else:
                dic2[value_t] = 1

        x = list(dic1.keys())

        Final = True
        for i in range(len(x)):
            if dic1[x[i]] != dic2.get(x[i],0):
                Final = False
        return Final

        