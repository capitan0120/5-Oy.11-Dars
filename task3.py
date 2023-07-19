class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        r = set(ransomNote)
        for i in r:
            if i not in magazine:
                return False
            else:
                if ransomNote.count(i) > magazine.count(i):
                    return False
        return True