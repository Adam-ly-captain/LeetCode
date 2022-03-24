# public class Solution {
#     public int[] TwoSum(int[] nums, int target) {
#         int[] dest = new int[2];
#         for (int i = 0; i < nums.Length; i++) {
#             for (int j = i + 1; j < nums.Length; j++) {
#                 if (nums[i] + nums[j] == target) {
#                     dest[0] = i;
#                     dest[1] = j;
#                     return dest;
#                 }
#             }
#         }
#         return null;
#     }
# }


class Solution(object):
    def twoSum(self, nums, target):
        src = {}
        for i in range(len(nums)):
            if nums[i] in src:
                return [src[nums[i]], i]
            src[target - nums[i]] = i
            
test = Solution()
res = test.twoSum([2,7,11,15], 9)
print(res)
