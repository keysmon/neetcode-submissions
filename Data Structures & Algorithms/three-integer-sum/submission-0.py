class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        n = len(nums)
        for start in range(n):
            if start>0 and nums[start] == nums[start-1]:
                continue
            l, r = start+1,n-1
            
            while l < r:
                cur_sum = nums[start] + nums[l] + nums[r]
                if cur_sum == 0:
                    res.append([nums[start],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif cur_sum >0:
                    r -= 1
                else:
                    l += 1
        return res
                
        
        