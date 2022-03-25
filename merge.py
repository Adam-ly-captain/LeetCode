class Solution(object):
    def merge(self, nums1, m, nums2, n):
        last = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0 :
            if nums1[m] > nums2[n] :
                nums1[last] = nums1[m]
                m -= 1
            else :
                nums1[last] = nums2[n]
                n -= 1
            last -= 1
        while n >= 0 :
            nums1[last] = nums2[n]
            n -= 1
            last -= 1
        return nums1  
        
            
        # for i in range(n) :
        #     nums1[m + i] = nums2[i]
        # nums1.sort()
        # return nums1
    
        # n1 = 0
        # n2 = 0
        # res = []
        # for i in range(m + n) :
        #     if nums1[n1] > nums2[n2] :
        #        res.append(nums2[n2])
        #        n2 += 1
        #     else :
        #         res.append(nums1[n1]) 
        #         n1 += 1
        #     if n1 == m or n2 == n:
        #         break
        # if n1 == m :
        #     for i in range(n2, n) :
        #         res.append(nums2[n2])
        #         n2 += 1
        # elif n2 == n :
        #     for i in range(n1, m) :
        #         res.append(nums1[n1])
        #         n1 += 1
        # return res

test = Solution()
res = test.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print(res)