class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        start = 0
        end = 0

        def _expand_around_center(left: int, right: int):
            """Expand from the center and return palindrome bounds"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            l1, r1 = _expand_around_center(i, i)
            l2, r2 = _expand_around_center(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start : end + 1]


s = input("Entre une chaîne : ")
sol = Solution()
result = sol.longestPalindrome(s)
print("Plus long palindrome :", result)
