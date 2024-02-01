from typing import List, Dict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h: Dict[List[str]] = {}

        for i, s in enumerate(strs):
            sstr = ''.join(sorted(s))

            if sstr in h:
                h[sstr].append(s)
            else:
                h[str(sstr)] = [s]

        return h.values()
    
Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])