import math
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        if len(s) != len(t):
            return False
        for i in range(0, len(s)):
            if s[i] not in d1:
                d1[s[i]]= 0
            if t[i] not in d1:
                d1[t[i]]= 0
            d1[s[i]]+=1
            d1[t[i]]-=1
            if s[i] in d1 and d1[s[i]]==0:
                d1.pop(s[i])
            if t[i] in d1 and d1[t[i]]==0:
                d1.pop(t[i])
        return len(d1)==0

if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("ana", "gram"))
    print(solution.isAnagram("ana", "ann"))
    print(solution.isAnagram("ana", "naa"))
    print(solution.isAnagram("listen", "silent"))
    print(solution.isAnagram("anagram", "nagaram"))
    print(solution.isAnagram("a", "ab"))
