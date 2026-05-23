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
        while i < len(s):
            num = ''
            #文字数を取得
            while s[i] != '#':
                #num = '' + '1'
                #num = '1'+'2'
                num += s[i]
                i += 1
            i += 1
            length = int(num)
            word = s[i:i+length]
            result.append(word)
            i += length
        return result

# Input: strs = ["Hello","World"]
# [5#Hello5#World]
# Output: ["Hello","World"]