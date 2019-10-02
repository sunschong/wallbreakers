class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #mapping of each char in s to each char in t
        print(set(zip(s, t))) 
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))