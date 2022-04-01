# class Solution():
#     def grayCode(self, n):
#         if n == 1:
#             return ['0', '1']
#         res = []
#         lastAppend = ' 0'
#         src = self.grayCode(n - 1)
#         for i in range(2 ** (n - 1)):
#             if lastAppend == ' 1':
#                 res.append(src[i] + ' 1')
#                 lastAppend = ' 1'
#             else:
#                 res.append(src[i] + ' 0')
#                 lastAppend = ' 0'
#             if lastAppend == ' 1':
#                 res.append(src[i] + ' 0')
#                 lastAppend = ' 0'
#             else:
#                 res.append(src[i] + ' 1')
#                 lastAppend = ' 1'
#         return res


# test = Solution()
# res = test.grayCode(4)
# print(res)
        
# class Solution():
    
#     flag = True
    
#     layer = 0
    
#     def grayCode(self, n):
#         if Solution.flag :
#             if n == 1:
#                 return [0, 1]
#             Solution.layer = n
#             Solution.flag = False
#         if n == 1:
#             return ['0', '1']
#         res = []
#         lastAppend = '0'
#         src = self.grayCode(n - 1)
#         for i in range(2 ** (n - 1)):
#             if lastAppend == '1':
#                 res.append(src[i] + '1')
#                 lastAppend = '1'
#             else:
#                 res.append(src[i] + '0')
#                 lastAppend = '0'
#             if lastAppend == '1':
#                 res.append(src[i] + '0')
#                 lastAppend = '0'
#             else:
#                 res.append(src[i] + '1')
#                 lastAppend = '1'
#         if Solution.layer == n:
#             for i in range(len(res)):
#                 res[i] = int(res[i], 2)
#         return res


# test = Solution()
# res = test.grayCode(1)
# print(res)
              
              
# class Solution():

#     def grayCode(self, n):
#         if n == 1:
#             return [0, 1]
#         res = []
#         lastAppend = '0'
#         src = self.grayCode(n - 1)
#         for i in range(2 ** (n - 1)):
#             if lastAppend == '1':
#                 res.append(int(bin(src[i])[2:] + '1', 2))
#                 lastAppend = '1'
#             else:
#                 res.append(int(bin(src[i])[2:] + '0', 2))
#                 lastAppend = '0'
#             if lastAppend == '1':
#                 res.append(int(bin(src[i])[2:] + '0', 2))
#                 lastAppend = '0'
#             else:
#                 res.append(int(bin(src[i])[2:] + '1', 2))
#                 lastAppend = '1'
#         return res

# class Solution():
    
#     # G(i) = i ^ (i >> 1)
    
#     def grayCode(self, n):
#         res = []
#         for i in range(2 ** n):
#             res.append(i ^ (i >> 1))
#         return res

class Solution():
    
    def grayCode(self, n):
        if n == 1:
            return [0, 1]
        res = self.grayCode(n - 1)
        src = [i for i in reversed(res)]
        length = len(res)
        for i in range(length):
            res.append(src[i] + length)
        return res


test = Solution()
res = test.grayCode(4)
print(res)
        