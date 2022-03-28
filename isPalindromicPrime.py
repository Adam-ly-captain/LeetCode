class Solution():
    def isLegal(self, num):
        if num <= 1 or isinstance(num, float):
            print('The data your input is illegal')
            return False
        else:
            return True
            
    
    def isPalindromic(self, num):
        src = num
        temp = 0
        while num > 0:
            temp = temp * 10 + num % 10
            num = num // 10
        if src == temp:
            return True
        else:
            return False
        
    
    def isPrime(self, num):
        dest = round(num ** 0.5)
        for i in range(2, dest + 1):
            if num % i == 0:
                return False
        else:
            return True
            
        
solution = Solution()
data = int(input())
if ~solution.isLegal(data):
    for i in range(2, data):
        if solution.isPrime(i) and solution.isPalindromic(i):
            print(i)
    

