class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        clean_list=[]
        for num in nums:
            if num!=val:
                clean_list.append(num)
        for i in range(len(clean_list)):
             nums[i]=clean_list[i]
        return len(clean_list)
        