class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        words = s.split()

        return len(words[-1])


s = input("Entre une chaîne : ")
sol = Solution()
print("Longueur du dernier mot :", sol.lengthOfLastWord(s))
