class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            key = sorted_str
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())
            
