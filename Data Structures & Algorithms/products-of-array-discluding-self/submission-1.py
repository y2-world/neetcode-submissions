class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        #配列の数の分繰り返し①
        #range() - for文でインデックス（カウンタ）を取得する
        for i in range(len(nums)):
            #掛け算の時は変数に1で初期化する
            product = 1
            #配列の数の分繰り返し②
            for j in range(len(nums)):
                #外のループのiと中のループのjが同じではない場合に掛ける
                if i != j:
                    #product = product * nums[j]
                    #product = 1 * 2 (nums[2]) = 2
                    #product = 2 * 4 (nums[3]) = 8
                    #product = 8 * 6 (nums[4]) = 48
                    product *= nums[j]
            #中のループが終了したら配列に追加
            result.append(product)
        return result