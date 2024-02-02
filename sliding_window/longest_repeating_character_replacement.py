class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        occurences = {}

        l = 0
        maxf = 0
        for r in range(len(s)):
            occurences[s[r]] = 1 + occurences.get(s[r], 0)
            maxf = max(maxf, occurences[s[r]])

            while (r - l + 1) - maxf > k:
                occurences[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


print(Solution().characterReplacement("ABAB", 2))