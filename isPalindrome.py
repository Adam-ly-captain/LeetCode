class Solution:
    def isPalindrome(self, x: int) -> bool:
        src = str(x)
        for i in range(len(src) // 2):
            if src[i : i + 1] != src[len(src) - i - 1 : len(src) - i]:
                return False
        else:
            return True