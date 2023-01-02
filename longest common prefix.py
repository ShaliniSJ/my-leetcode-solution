class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res =''
        strs = zip(*strs)
        for i in list(strs):
            if len(set(i)) == 1:
                res+=str(i[0])
            else:break
        return res
