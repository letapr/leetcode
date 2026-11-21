# dict keys: first original word in a set of anagramous words. value: all existing anagrams to the key
# compare new word against existing keys until either it can be categorized or if it cannot, is created as a key
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d1 = {}
        added=False
        for i in range(0,len(strs)):
            for key in d1:
                if self.isAnagram(strs[i], key):
                    d1[key].append(strs[i])
                    added=True
                    break
            if added==False: 
                d1[strs[i]]=[strs[i]]
            added=False
        return list(d1.values())
            
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for num in count:
            if num != 0:
                return False

        return True

if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))