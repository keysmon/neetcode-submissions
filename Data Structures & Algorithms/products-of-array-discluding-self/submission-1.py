class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1]*len(nums)
        suffix_product = [1]*len(nums)
        prefix_product[0],suffix_product[-1] = nums[0], nums[-1]
        for idx in range(len(nums)-1):
            prefix_product[idx+1] = prefix_product[idx] * nums[idx+1]
        for idx in range(len(nums)-2, -1,-1):
            suffix_product[idx] = suffix_product[idx+1] * nums[idx]
       
        res = []
        for idx in range(len(nums)):
            prefix = prefix_product[idx-1] if idx > 0 else 1
            suffix = suffix_product[idx+1] if idx < len(nums)-1 else 1
            res.append(prefix*suffix)

        return res