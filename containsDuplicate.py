class Solution(object):
    def containsDuplicate(self, nums):
        temp = {}
       	for i in range(len(nums)):
            temp[nums[i]] = i    
        return True if len(temp.keys()) < len(nums) else False
              
           
       
test = Solution()
res =  test.containsDuplicate([1, 2, 3, 1])
print(res)
