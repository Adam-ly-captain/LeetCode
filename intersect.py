class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        for i in range(len(nums2)) :
            if nums2[i] in nums1 :
                res.append(nums2[i])
                nums1.remove(nums2[i])
        return res


test = Solution()
res = test.intersect([4,4,9,5], [9,4,9,8,4])
print(res)