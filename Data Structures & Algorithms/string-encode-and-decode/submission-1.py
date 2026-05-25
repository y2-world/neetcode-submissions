class Solution:

    def encode(self, strs: List[str]) -> str:
        strList = []
        for word in strs:
            newStr = str(len(word)) + '#' + word
            strList.append(newStr)
        return ''.join(strList)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        #0 < 14
        while i < len(s):
            num = ''
            #'#'が来るまで繰り返す
            while s[i] != '#':
                #num = '5'
                num += s[i]
                i += 1
            #i = 1+1
            i += 1
            length = int(num)
            #s[2:2+5] : 2から7の手前まで取得
            word = s[i:i+length]
            #配列resultにwordを追加
            result.append(word)
            #次の文字に移動 (i = 2+5)
            i += length
        return result

