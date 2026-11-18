class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        prev = nums[0]
        cur = max(nums[0], nums[1])

        for i in range(2,len(nums)):
            temp = cur
            cur = max(prev + nums[i], cur)
            prev = temp
        return cur 
