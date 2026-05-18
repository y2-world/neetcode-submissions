class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #重複なしの空配列を生成
        seen = set()
        for num in nums:
            #numにseenの中に存在したらtrue
            if num in seen:
                return True
            #重複なしの空配列に数値numを追加
            seen.add(num)
        return False