class Solution:
    #right if less then current (positive)
    #left is less current (negative)
    def romanToInt(self, s: str) -> int:
        rom = {'I':1 , 'V' :5 , 'X' :10 , 'L':50 , 'C':100 , 'D':500 , 'M' : 1000}
        sum = 0
        for i in range(len(s)):
            if i+1 < len(s) and rom[s[i]] < rom[s[i+1]]:
                sum -= rom[s[i]]
            else :
                sum += rom[s[i]]
        return sum
