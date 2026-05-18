class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #重複なしの空配列を生成
        seen = set()
        for num in nums:
            #seenにnumと同じ値が存在したらtrue
            if num in seen:
                return True
            #seenに数値numを追加
            seen.add(num)
        return False

# 1 in {}
# 2 in {1}
# 3 in {1,2}
# 3 in {1,2,3} - true

# 1 in {}
# 2 in {1}
# 3 in {1,2}
# 4 in {1,2,3} 
# false