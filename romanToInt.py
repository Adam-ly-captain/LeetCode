# class Solution(object):
#     def romanToInt(self, s):
#         res = 0
#         roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
#         for i in range(len(s)):
#             op = 1  # 1 表示加 , 0 表示减
#             if i + 1 != len(s) and s[i : i + 1] == 'I':
#                 if s[i + 1 : i + 2] == 'V' or s[i + 1 : i + 2] == 'X':
#                     op = 0
#             elif i + 1 != len(s) and s[i : i + 1] == 'X':
#                 if s[i + 1 : i + 2] == 'L' or s[i + 1 : i + 2] == 'C':
#                     op = 0
#             elif i + 1 != len(s) and s[i : i + 1] == 'C':
#                 if s[i + 1 : i + 2] == "D" or s[i + 1 : i + 2] == 'M':
#                     op = 0
#             if op == 1 :
#                res += roman[s[i : i + 1]] 
#             else :
#                 res -= roman[s[i : i + 1]]
#         return res

class Solution(object):
    def romanToInt(self, s):
        res = 0
        roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]] :
                res -= roman[s[i]]
            else :
                res += roman[s[i]]
        return res

s = "XXVII"
test = Solution()
res = test.romanToInt(s)
print(res)
