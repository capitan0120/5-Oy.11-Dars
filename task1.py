class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        while num>i*i:
            i += 1
            if i*i == num:
                return True
        return False