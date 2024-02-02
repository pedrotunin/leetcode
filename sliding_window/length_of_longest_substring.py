class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        maxLength = 1
        l = 0
        seen = {}

        for r in range(len(s)):
            c = s[r]
            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            else:
                maxLength = max(maxLength, r - l + 1)
            seen[c] = r

        return maxLength

print(Solution().lengthOfLongestSubstring("tmmzuxt"))