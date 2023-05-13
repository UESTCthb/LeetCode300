class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = len(nums)
        l = len(nums)
        i = 0
        while i<l:
            if nums[i]==val:
                for j in range(i+1,l):
                    nums[j-1] = nums[j]
                l-=1
                i-=1
            i+=1
        return l
