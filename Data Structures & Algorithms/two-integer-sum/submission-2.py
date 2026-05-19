class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                #seenに存在するdiffと同じ値のindexを返す
                return [nums.index(diff), i]
            #ループした値のdictをseenに代入
            seen[num] = i 