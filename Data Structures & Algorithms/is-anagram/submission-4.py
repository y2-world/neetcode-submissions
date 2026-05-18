class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sortedS = sorted(s)
        # sortedT = sorted(t)
        if sorted(s) == sorted(t):
            return True
        else:
            return False

        # if len(sortedS) != len(sortedT):
        #     return False
        # for i, sS in enumerate(sortedS):
        #     if sS != sortedT[i]:
        #         return False
        # return True

            
        