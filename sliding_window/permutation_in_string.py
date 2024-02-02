class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        ocurrences_in_s1 = {}

        for c in s1:
            ocurrences_in_s1[c] = 1 + ocurrences_in_s1.get(c, 0)

        ocurrences = {}
        window_size = len(s1)

        for r in range(len(s2)):
            ocurrences[s2[r]] = 1 + ocurrences.get(s2[r], 0)

            if ocurrences_in_s1.items() == ocurrences.items():
                return True
            
            if r >= window_size - 1:
                i = s2[r - (window_size - 1)]
                ocurrences[i] -= 1
                if ocurrences[i] == 0:
                    ocurrences.pop(i)
        
        return False



print(Solution().checkInclusion(s1="ab", s2="eidboaoo"))