class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        for i in range(n + 1):
            found = False
            for num in nums:
                if num == i:
                    found = True
                    break
            if found == False:
                return i