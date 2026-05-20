class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            #１文字ずつの配列を文字列に連結する
            key = ''.join(sorted(s))
            #未登録の場合、キー用の空リストを作る
            if key not in groups:
                groups[key] = []
            #ソートしたキーのdictに元々の文字列をvalueとして追加
            groups[key].append(s)
        return list(groups.values())

#key = act
#groups = {"aet": []}
#groups = {"aet": ["eat"]}

#s = pots
#key = opst
#groups = {"aet": [], "opst": []}
#groups = {"aet": ["eat"], "opst": ["pots"]}