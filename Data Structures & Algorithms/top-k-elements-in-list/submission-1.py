class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            #.get: キーから値を取得
            #seenにnumをキーとしたdictを代入
            seen[num] = seen.get(num, 0) + 1
            #seenを降順にdictのvalueで並べてk個スライス
        return sorted(seen,key=seen.get, reverse=True)[:k]

# seen[1] = {1:1}      
# seen[2] = {2:1}    
# seen[2] = {2:2}  
# seen[3] = {3:1}    
# seen[3] = {3:2}   
# seen[3] = {3:3}    

# {1:1, 2:2, 3:3}
# {3:3, 2:2, 1:1}
# [3,2,1][:2]
# [3,2]
        