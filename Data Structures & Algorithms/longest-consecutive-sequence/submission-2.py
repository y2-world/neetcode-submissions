class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        else:
            nums.sort()
            count = 1
            max_count = 1
            #1から順番に数字の数分繰り返す
            for i in range(1, len(nums)):
                #前の数字に1足した数と等しい場合はカウント
                if nums[i] == nums[i - 1] + 1:
                    count += 1
                #前の数字と等しい場合(同じ数)はスキップ
                elif nums[i] == nums[i - 1]:
                    continue
                #それ以外はカウントをリセット
                else:
                    count = 1
                #max_countとcount(現時点のカウント)を比較
                max_count = max(max_count, count)
            return max_count
        

        # numList = []
        # for i, num in enumerate(nums):
        #    for j, num in enumerate(nums):
        #         if nums[i] != nums[j]:
        #             continue
        #         if nums[i] - nums[j] == abs(1):
        #             numList.append(nums[i])
        #             return True
        # return result